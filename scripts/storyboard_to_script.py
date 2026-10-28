"""장면 구성표(03_storyboard.json)에서 사람이 읽기 좋은 대본(02_script.md)을 만든다."""
import json
import sys
from pathlib import Path

CHARS_PER_MIN = 320  # 한국어 나레이션 1분당 글자 수 (스타일 가이드 기준)

ep = Path(sys.argv[1])
sb = json.loads((ep / "03_storyboard.json").read_text(encoding="utf-8"))

lines = [f"# {sb['title']}", "", f"- 개념: {sb['concept']} · {sb['curriculum']} · 난이도 `{sb['level']}`"]
total = 0
body = []
section = None
for sc in sb["scenes"]:
    if sc["section"] != section:
        section = sc["section"]
        body += ["", f"## {section}"]
    body += ["", f"**[장면 {sc['id']}]** `[화면: {sc['visual']['description']}]`"]
    if sc.get("on_screen_text"):
        body.append(f"`[강조: {sc['on_screen_text']}]`")
    for n in sc["narration"]:
        text = n.get("sub", n["say"])
        total += len(n["say"])
        body.append(f"> {text}")
lines.append(f"- 나레이션 분량: {total}자 (공백 포함, 예상 약 {total / CHARS_PER_MIN:.1f}분)")
(ep / "02_script.md").write_text("\n".join(lines + body) + "\n", encoding="utf-8")
print(total)
