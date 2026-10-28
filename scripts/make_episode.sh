#!/usr/bin/env bash
# 에피소드 하나를 처음부터 끝까지 자동으로 만든다.
# 사용법: scripts/make_episode.sh episodes/<날짜>_<slug>
#   입력: 03_storyboard.json, visuals.py, assets/media/ (AI 소재는 제작팀이 미리 생성해 둔다)
#   출력: 02_script.md, output/final.mp4, output/subtitles.srt
#   음성 엔진: CHOIGO_TTS_ENGINE=clova(기본) | mimic3(테스트 전용)
set -euo pipefail

EP="$1"
DIR="$(cd "$(dirname "$0")" && pwd)"
PY="${CHOIGO_PYTHON:-/opt/choigo-venv/bin/python}"

echo "① 대본 정리";            python3 "$DIR/storyboard_to_script.py" "$EP"
echo "② 나레이션 합성";        "$PY" "$DIR/tts.py" "$EP" 2>/dev/null | tail -1
echo "③ 발음 점검";            "$PY" "$DIR/check_narration.py" "$EP" 2>/dev/null > "$EP/assets/audio/pronunciation_check.txt"
                               head -1 "$EP/assets/audio/pronunciation_check.txt"
echo "④ 실사 소재 수집";       python3 "$DIR/fetch_media.py" "$EP"
echo "⑤ 장면 렌더링";          "$DIR/render_scenes.sh" "$EP" | { ! grep FAIL; }
echo "⑥ 합성 (배경, 자막, 음악)"; "$PY" "$DIR/assemble.py" "$EP"
