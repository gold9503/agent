"""영상 DB 관리 (기술지원팀).

사용법:
  python scripts/db.py add <에피소드 폴더> --status 보류
  python scripts/db.py review <에피소드 폴더> <차수> <판정> [메모]
  python scripts/db.py list
  python scripts/db.py has <개념 이름>     # 이미 다룬 개념인지 확인
"""
import argparse
import json
import shutil
import sqlite3
import subprocess
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data/choigo.db"
SCHEMA = ROOT / "scripts/db/schema.sql"


def connect():
    if DB.exists():
        backup = ROOT / "data/backup"
        backup.mkdir(parents=True, exist_ok=True)
        shutil.copy2(DB, backup / f"choigo-{date.today()}.db")
    con = sqlite3.connect(DB)
    con.executescript(SCHEMA.read_text(encoding="utf-8"))
    return con


def duration(path):
    if not path.exists():
        return None
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                         capture_output=True, text=True).stdout
    return round(float(out), 1)


def episode_id(con, folder):
    return con.execute("SELECT id FROM episodes WHERE slug = ?", (Path(folder).name,)).fetchone()[0]


def cmd_add(con, a):
    ep = Path(a.episode).resolve()
    sb = json.loads((ep / "03_storyboard.json").read_text(encoding="utf-8"))
    con.execute("INSERT INTO concepts (name, subject, level, curriculum) VALUES (?, ?, ?, ?) "
                "ON CONFLICT(name) DO UPDATE SET subject=excluded.subject, level=excluded.level, "
                "curriculum=excluded.curriculum",
                (sb["concept"], sb["subject"], sb["level"], sb["curriculum"]))
    cid = con.execute("SELECT id FROM concepts WHERE name = ?", (sb["concept"],)).fetchone()[0]
    con.execute("INSERT INTO episodes (concept_id, made_on, slug, title, duration_sec, status, folder) "
                "VALUES (?, ?, ?, ?, ?, ?, ?) ON CONFLICT(slug) DO UPDATE SET title=excluded.title, "
                "duration_sec=excluded.duration_sec, status=excluded.status",
                (cid, ep.name[:10], ep.name, sb["title"], duration(ep / "output/final.mp4"), a.status,
                 str(ep.relative_to(ROOT))))
    eid = episode_id(con, ep)
    src = ep / "assets/sources.json"
    if src.exists():
        con.execute("DELETE FROM assets WHERE episode_id = ?", (eid,))
        for s in json.loads(src.read_text(encoding="utf-8"))["assets"]:
            con.execute("INSERT INTO assets (episode_id, type, files, source, author, license) VALUES (?,?,?,?,?,?)",
                        (eid, s["type"], s.get("file") or s.get("files"), s.get("source"), s.get("author"),
                         s.get("license")))
    print(f"기록: {ep.name} ({a.status})")


def cmd_review(con, a):
    eid = episode_id(con, a.episode)
    con.execute("INSERT INTO legal_reviews (episode_id, round, verdict, reviewed_on, notes) VALUES (?,?,?,?,?) "
                "ON CONFLICT(episode_id, round) DO UPDATE SET verdict=excluded.verdict, notes=excluded.notes",
                (eid, a.round, a.verdict, str(date.today()), a.notes))
    print(f"법무 {a.round}차: {a.verdict}")


def cmd_list(con, a):
    rows = con.execute("SELECT e.made_on, c.subject, c.name, e.status, e.duration_sec FROM episodes e "
                       "JOIN concepts c ON c.id = e.concept_id ORDER BY e.made_on").fetchall()
    for r in rows:
        print(" | ".join("" if v is None else str(v) for v in r))


def cmd_has(con, a):
    r = con.execute("SELECT e.slug, e.status FROM concepts c JOIN episodes e ON e.concept_id = c.id "
                    "WHERE c.name LIKE ?", (f"%{a.name}%",)).fetchall()
    print("\n".join(f"이미 있음: {s} ({st})" for s, st in r) or "아직 다루지 않음")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("add"); p.add_argument("episode"); p.add_argument("--status", default="제작")
    p = sub.add_parser("review"); p.add_argument("episode"); p.add_argument("round", type=int)
    p.add_argument("verdict"); p.add_argument("notes", nargs="?")
    sub.add_parser("list")
    p = sub.add_parser("has"); p.add_argument("name")
    a = ap.parse_args()
    con = connect()
    {"add": cmd_add, "review": cmd_review, "list": cmd_list, "has": cmd_has}[a.cmd](con, a)
    con.commit()


if __name__ == "__main__":
    main()
