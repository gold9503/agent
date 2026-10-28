"""장면 구성표의 "media" 목록에 있는 실사 소재를 모으고 출처를 기록한다.

소재 종류 (03_storyboard.json → "media": {id: {...}})
  commons  위키미디어 커먼즈 파일      {"source": "commons", "ref": "File:....jpg"}
  met      메트로폴리탄 미술관 공개자료  {"source": "met", "query": "cuneiform tablet"}  또는 {"source": "met", "ref": "<objectID>"}
  ai       AI 생성 영상/이미지          {"source": "ai", "kind": "video|image", "prompt": "...", "model": "...",
                                       "job_id": "...", "url": "..."}
           → 제작팀이 Higgsfield로 만들어 assets/media/<id>.mp4|.png 로 저장하고, 모델·작업 ID·URL을
             구성표에 적어 둔다(다시 받을 수 있게). 이 스크립트는 파일이 있는지만 확인한다.

비상업(NC)·변경금지(ND) 라이선스는 자동으로 거부한다.
출력: assets/media/<id>.*, assets/sources.json
사용법: python fetch_media.py <에피소드 폴더>
"""
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

UA = {"User-Agent": "ChoigoStudy/1.0 (educational video pipeline)"}
COMMONS_API = "https://commons.wikimedia.org/w/api.php"
MET_API = "https://collectionapi.metmuseum.org/public/collection/v1"
BLOCKED = ("NC", "ND", "noncommercial", "no derivatives")

STATIC_SOURCES = [
    {"id": "animation", "type": "animation", "source": "자체 제작 (visuals.py, Manim)", "author": "최고의 공부",
     "license": "자체 저작물", "ai": False},
    {"id": "bgm", "type": "music", "source": "자체 합성 (scripts/bgm.py)", "author": "최고의 공부",
     "license": "자체 저작물", "ai": False},
    {"id": "fonts", "type": "font", "source": "Noto Sans/Serif CJK KR, Computer Modern", "author": "Google, Adobe / D. Knuth",
     "license": "SIL OFL 1.1 / Knuth License", "ai": False},
]


def get_json(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        return json.load(r)


def download(url, dest):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r:
        dest.write_bytes(r.read())


def strip_html(s):
    import re
    return re.sub(r"<[^>]+>", "", s or "").strip()


def from_commons(mid, m, out):
    q = urllib.parse.urlencode({"action": "query", "titles": m["ref"], "prop": "imageinfo", "format": "json",
                                "iiprop": "url|extmetadata", "iiurlwidth": 2400})
    page = next(iter(get_json(f"{COMMONS_API}?{q}")["query"]["pages"].values()))
    if "imageinfo" not in page:
        raise RuntimeError(f"커먼즈에 파일이 없습니다: {m['ref']}")
    info = page["imageinfo"][0]
    meta = info.get("extmetadata", {})
    lic = meta.get("LicenseShortName", {}).get("value", "unknown")
    if any(b.lower() in lic.lower() for b in BLOCKED):
        raise RuntimeError(f"사용 불가 라이선스: {lic}")
    url = info.get("thumburl") or info["url"]
    dest = out / f"{mid}{Path(urllib.parse.urlparse(url).path).suffix.lower() or '.jpg'}"
    download(url, dest)
    return dest, {"source": info["descriptionurl"], "author": strip_html(meta.get("Artist", {}).get("value")),
                  "credit": strip_html(meta.get("Credit", {}).get("value")), "license": lic}


def from_met(mid, m, out):
    ids = [m["ref"]] if "ref" in m else get_json(
        f"{MET_API}/search?{urllib.parse.urlencode({'q': m['query'], 'hasImages': 'true'})}").get("objectIDs") or []
    for oid in ids[:40]:
        o = get_json(f"{MET_API}/objects/{oid}")
        if o.get("isPublicDomain") and o.get("primaryImage"):
            dest = out / f"{mid}.jpg"
            download(o["primaryImage"], dest)
            return dest, {"source": o["objectURL"], "author": "The Metropolitan Museum of Art",
                          "credit": f"{o.get('title')} ({o.get('objectDate')})", "license": "CC0 (Met Open Access)"}
    raise RuntimeError(f"공개(CC0) 이미지를 찾지 못했습니다: {m.get('query', m.get('ref'))}")


def main():
    ep = Path(sys.argv[1])
    sb = json.loads((ep / "03_storyboard.json").read_text(encoding="utf-8"))
    out = ep / "assets/media"
    out.mkdir(parents=True, exist_ok=True)
    src_path = ep / "assets/sources.json"
    old = {s["id"]: s for s in json.loads(src_path.read_text(encoding="utf-8")).get("assets", [])} \
        if src_path.exists() else {}

    tts = (ep / "assets/audio/engine.txt")
    entries = list(STATIC_SOURCES)
    if tts.exists():
        engine = tts.read_text().split()
        entries.append({"id": "narration", "type": "tts_voice", "ai": True,
                        "source": "NAVER Cloud CLOVA Voice Premium" if engine[0] == "clova" else "mimic3 ko_KO kss_low",
                        "author": engine[1] if len(engine) > 1 else "", "license":
                        "NAVER Cloud 이용약관 (법무팀 확인)" if engine[0] == "clova" else "모델 CC0 / 학습 데이터 비영리 → 테스트 전용"})

    problems = []
    for mid, m in sb.get("media", {}).items():
        try:
            if m["source"] == "ai":
                files = [p for p in out.glob(f"{mid}.*")]
                if not files:
                    raise RuntimeError(f"AI 소재가 아직 없습니다. 프롬프트: {m['prompt']}")
                entries.append({"id": mid, "type": m.get("kind", "video"), "file": str(files[0].relative_to(ep)),
                                "source": f"AI 생성 ({m.get('model', 'Higgsfield')})", "prompt": m["prompt"],
                                "job_id": m.get("job_id"), "url": m.get("url"),
                                "author": "최고의 공부 (AI 도구 사용)", "license": "생성 서비스 약관 (법무팀 확인)", "ai": True})
                continue
            if mid in old and (ep / old[mid].get("file", "-")).exists():
                entries.append(old[mid])
                continue
            dest, info = (from_commons if m["source"] == "commons" else from_met)(mid, m, out)
            entries.append({"id": mid, "type": "image", "file": str(dest.relative_to(ep)), "ai": False, **info})
            print(f"ok {mid}: {info['license']}")
        except Exception as e:  # noqa: BLE001 - 소재 하나가 실패해도 나머지는 계속 모은다
            problems.append(f"{mid}: {e}")

    src_path.write_text(json.dumps({"episode": ep.name, "assets": entries}, ensure_ascii=False, indent=2),
                        encoding="utf-8")
    for p in problems:
        print("MISSING", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
