#!/usr/bin/env bash
# 「최고의 공부」 제작 환경 설치 (Ubuntu 24.04 기준). 기술지원팀 관리.
set -euo pipefail

# 1) 시스템 패키지: 한글 폰트, Manim 의존성(cairo/pango), 수식용 LaTeX, ffmpeg
sudo apt-get update -qq
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -qq \
  ffmpeg fonts-noto-cjk libcairo2-dev libpango1.0-dev pkg-config \
  texlive-latex-base texlive-latex-extra texlive-fonts-recommended dvisvgm cm-super

# 2) 파이썬 가상환경 (Manim, TTS)
#    sherpa-onnx 2.x는 mimic3 한국어 음성의 발음 변환을 지원하지 않아 1.12.40으로 고정
python3 -m venv /opt/choigo-venv
/opt/choigo-venv/bin/pip install -q -U pip setuptools wheel
/opt/choigo-venv/bin/pip install -q manim==0.22.1 "sherpa-onnx==1.12.40" soundfile

# 3) 모델: 한국어 TTS(임시, 비공개 테스트용)와 발음 점검용 한국어 음성 인식
mkdir -p /opt/choigo-models && cd /opt/choigo-models
base=https://github.com/k2-fsa/sherpa-onnx/releases/download
for m in tts-models/vits-mimic3-ko_KO-kss_low asr-models/sherpa-onnx-zipformer-korean-2024-06-24; do
  name=$(basename "$m")
  [ -d "$name" ] || { curl -sSL -o "$name.tar.bz2" "$base/$m.tar.bz2" && tar xjf "$name.tar.bz2" && rm "$name.tar.bz2"; }
done
echo "설치 완료"
