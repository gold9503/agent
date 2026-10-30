#!/usr/bin/env bash
# 에피소드 하나를 처음부터 끝까지 자동으로 만든다.
# 사용법: scripts/make_episode.sh episodes/<날짜>_<slug>
#   입력: 03_storyboard.json, visuals.py, assets/media/ (AI 소재는 제작팀이 미리 생성해 둔다),
#         assets/audio/elevenlabs/scene_XX.mp3 (ElevenLabs 커넥터로 미리 생성, 원고는 tts.py --prompts)
#   출력: 02_script.md, output/final.mp4, output/subtitles.srt
#   음성 엔진: CHOIGO_TTS_ENGINE=elevenlabs(기본) | clova(예비) | mimic3(테스트 전용)
#   미리보기: CHOIGO_ALLOW_MISSING_MEDIA=1 이면 빠진 실사 소재를 기본 배경으로 대체 (공개용 금지)
set -euo pipefail

EP="$1"
DIR="$(cd "$(dirname "$0")" && pwd)"
PY="${CHOIGO_PYTHON:-/opt/choigo-venv/bin/python}"

echo "① 대본 정리";            python3 "$DIR/storyboard_to_script.py" "$EP"
echo "② 나레이션 합성";        "$PY" "$DIR/tts.py" "$EP" 2>/dev/null | tail -1
echo "③ 발음 점검";            "$PY" "$DIR/check_narration.py" "$EP" 2>/dev/null > "$EP/assets/audio/pronunciation_check.txt"
                               head -1 "$EP/assets/audio/pronunciation_check.txt"
echo "④ 실사 소재 수집";       python3 "$DIR/fetch_media.py" "$EP" ${CHOIGO_ALLOW_MISSING_MEDIA:+--allow-missing}
echo "⑤ 장면 렌더링";          "$DIR/render_scenes.sh" "$EP" | { ! grep FAIL; }
echo "⑥ 합성 (배경, 자막, 음악)"; "$PY" "$DIR/assemble.py" "$EP"
if grep -q '"shorts"' "$EP/03_storyboard.json" && ! grep -q '"format": *"vertical"' "$EP/03_storyboard.json"; then
echo "⑦ 숏폼 (세로 9:16, 정사각형 1:1)"; (cd "$DIR" && "$PY" make_shorts.py "$EP")
fi
