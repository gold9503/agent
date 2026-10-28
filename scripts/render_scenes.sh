#!/usr/bin/env bash
# 에피소드의 visuals.py 장면들을 병렬로 렌더링한다.
# 사용법: scripts/render_scenes.sh episodes/<날짜>_<slug> [장면번호...]
set -euo pipefail

EP="$(cd "$1" && pwd)"
shift
PY="${CHOIGO_PYTHON:-/opt/choigo-venv/bin/python}"
JOBS="${CHOIGO_JOBS:-4}"
export CHOIGO_EPISODE="$EP"
export PYTHONPATH="$(cd "$(dirname "$0")" && pwd)${PYTHONPATH:+:$PYTHONPATH}"

if [ "$#" -gt 0 ]; then
  SCENES=$(printf "S%02d\n" "$@")
else
  SCENES=$(grep -oE '^class (S[0-9]{2})\(' "$EP/visuals.py" | sed -E 's/class (S[0-9]+)\(/\1/')
fi

mkdir -p "$EP/assets/render/logs"
echo "$SCENES" | xargs -P "$JOBS" -I{} sh -c \
  "'$PY' -m manim render -t -q h --fps 30 -r 1920,1080 --disable_caching --media_dir '$EP/assets/render/{}' \
   '$EP/visuals.py' {} > '$EP/assets/render/logs/{}.log' 2>&1 && echo 'ok {}' || echo 'FAIL {}'"
