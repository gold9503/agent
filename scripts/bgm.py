"""잔잔한 배경음악을 직접 합성한다 (외부 음원 없음 → 저작권 문제 없음).

느린 화음 패드(Am - F - C - G) + 낮은 베이스 + 간단한 잔향.
사용법: python bgm.py <출력.wav> <길이(초)>
"""
import sys

import numpy as np
import soundfile as sf

SR = 44100
CHORDS = [  # (베이스, 화음 구성음) 단위 Hz
    (110.00, [220.00, 261.63, 329.63]),   # Am
    (87.31, [174.61, 220.00, 261.63]),    # F
    (130.81, [196.00, 261.63, 329.63]),   # C
    (98.00, [196.00, 246.94, 293.66]),    # G
]
BAR = 8.0  # 화음 하나의 길이(초)


def voice(freq, n, rng):
    t = np.arange(n) / SR
    out = np.zeros(n)
    for detune in (-0.12, 0.0, 0.12):             # 살짝 어긋난 음을 겹쳐 부드럽게
        f = freq * (1 + detune / 100)
        ph = rng.uniform(0, 2 * np.pi)
        out += np.sin(2 * np.pi * f * t + ph) + 0.18 * np.sin(4 * np.pi * f * t + ph)
    return out / 3


def envelope(n, attack=2.5, release=3.0):
    env = np.ones(n)
    a, r = int(attack * SR), int(release * SR)
    env[:a] = np.linspace(0, 1, a) ** 2
    env[-r:] = np.linspace(1, 0, r) ** 2
    return env


def reverb(x, delays=(0.031, 0.047, 0.061, 0.083), fb=0.55):
    y = x.copy()
    for d in delays:
        k = int(d * SR)
        buf = np.zeros_like(x)
        for i in range(k, len(x), k):
            j = min(i + k, len(x))
            buf[i:j] = (x[i - k:j - k] + fb * buf[i - k:j - k])[: j - i]
        y += 0.25 * buf
    return y


def main():
    out, length = sys.argv[1], float(sys.argv[2])
    rng = np.random.default_rng(28)
    n_total = int(length * SR)
    mix = np.zeros(n_total + int(4 * SR))
    seg = int((BAR + 3.0) * SR)            # 다음 화음과 3초 겹치게
    t0 = 0
    k = 0
    while t0 < n_total:
        bass, notes = CHORDS[k % len(CHORDS)]
        n = min(seg, len(mix) - t0)
        s = sum(voice(f, n, rng) for f in notes) / len(notes)
        s += 0.6 * voice(bass, n, rng)
        mix[t0:t0 + n] += s * envelope(n)[:n]
        t0 += int(BAR * SR)
        k += 1
    mix = reverb(mix[:n_total])
    # 전체 페이드 인/아웃
    fade = int(3 * SR)
    mix[:fade] *= np.linspace(0, 1, fade)
    mix[-fade:] *= np.linspace(1, 0, fade)
    mix /= np.max(np.abs(mix)) + 1e-9
    stereo = np.stack([mix, np.roll(mix, int(0.012 * SR))], axis=1) * 0.5
    sf.write(out, stereo.astype(np.float32), SR)


if __name__ == "__main__":
    main()
