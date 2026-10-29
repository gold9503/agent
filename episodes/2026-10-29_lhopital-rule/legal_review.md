# 법무 검토: 로피탈의 정리: 0/0은 빠르기 대결이다 (1차: 대본)

판정: **조건부 통과**

위험도 상은 없다. 아래 중 항목(1, 2, 9, 12, 15)은 해당 단계 전에 반드시 해소해야 한다. 1, 2는 제작 착수 전, 12는 나레이션 생성 전, 9와 15는 2차 검토 전이다.

> 이 검토는 위험을 줄이기 위한 사내 점검이며 법률 자문을 대신하지 않는다.
> 이번 세션에서는 mathshistory.st-andrews.ac.uk, commons.wikimedia.org, secure-media.collegeboard.org, rd.springer.com, elevenlabs.io를 **열지 못했다**(접속 불가). 아래에서 "원문 미열람"이라고 적은 항목은 웹 검색 결과와 미러 사이트로만 교차 확인한 것이다.

## 사실관계 점검

### 기획팀 확인 요청 항목
| # | 항목 | 결론 | 근거와 한계 |
|---|---|---|---|
| ① | 1694년 3월 편지, "해마다 300리브르" | **통과** | 300이라는 숫자와 연간 지급(pension)은 College Board 번역, MacTutor, Wikipedia, Springer 초록 요약이 모두 일치한다. "300 pounds", "three hundred French pounds"는 livre를 영어로 옮긴 말이다(livre = pound). "Francs"는 당시 계산 단위로 맞지 않는다. 그래서 "리브르"가 맞다. 참고: 번역에 따르면 첫해 상반기는 이미 받은 글값을 더해 200리브르, 이후 반기마다 150리브르다. "해마다 300리브르"라는 요지는 정확하다. 편지에는 바리뇽 등 다른 사람에게 보내지 말라는 요청도 있어서 "자신에게만"이라는 요지도 맞다. **원문 미열람**(프랑스어 원문, MacTutor, College Board PDF 모두 열지 못함) |
| ② | 1694년 7월 베르누이 편지에 0/0 규칙 | **통과** | Springer 역주본 12장 초록 요약("the letter of July 22, 1694, where L'Hôpital's Rule appears for the first time")과 Wikipedia가 일치한다. **원문 미열람** |
| ③ | "미분을 다룬 최초의 교과서" | **통과** | MacTutor("the first text-book to be written on the differential calculus"), Wikipedia, Springer 소개가 일치한다. 학계에서 널리 쓰는 평가라서 단정해도 무리는 없다. 더 조심하려면 "최초의 교과서로 꼽히는"이라고 써도 된다(선택 사항) |
| ④ | 정리의 주인 문제를 공정하게 썼는가 | **통과** | 대본은 사실(유료 계약 제안, 7월 편지, 책에 실림, 머리말에서 도움을 밝힘)만 순서대로 말한다. "샀다", "훔쳤다", "베꼈다" 같은 단정이 없다. 머리말에서 도움을 밝혔다는 문장이 균형을 잡아 준다(Wikipedia도 이 머리말을 근거로 "로피탈이 공을 가로채려 했다"는 주장은 부정확하다고 쓴다). 300년 전 인물이고 모두 확인된 사실이라 명예훼손 위험은 낮다. 장면 4 둘째 문장은 시점을 단정하므로 지적 4로 다듬는다 |
| ⑤ | 머리말에서 베르누이의 도움을 밝혔다 | **통과** | 1730년 영어 번역의 머리말 인용("I must own my self very much obliged to the Labours of Messieurs Bernoulli, but particularly to those of the present Professor at Groenengen"), Truesdell의 서술, Wikipedia가 일치한다. 1690년대에 흐로닝언 교수였던 사람은 요한 베르누이다. 화면 메모 '라이프니츠, 베르누이 형제에게 감사'도 맞다. **MacTutor 머리말 번역 원문 미열람** |
| ⑥ | 커먼즈 파일 3개 | **조건부** | 지적 9~11 참고 |
| ⑦ | AI 재현 영상 5개 | **조건부** | 지적 1~3 참고. 장면 4뿐 아니라 **장면 1**(study_desk_night)에도 AI 표시가 빠져 있다 |

### 그 밖의 사실
- 1696년 출간, 익명 출간, 1715년 판이 제2판(Paris, F. Montalant)이라는 점은 검색 결과와 일치한다.
- 요한 베르누이(1667~1748)는 1694년에 26~27세였고 바젤 출신이므로 "스위스의 젊은 수학자"는 맞다.
- 참고: 리서치 노트는 베르누이 강의록 사본 발견을 1922년으로 적었고, 검색 결과에는 1921년(Schafheitlin)으로 나온다. 대본에 쓰지 않으므로 문제는 없다. 다만 기획팀은 리서치 노트를 "1921년(자료에 따라 1922년)"으로 고쳐 두기 바란다.

### 수학 검산 (직접 계산)
- **장면 6 (선형 근사):** f(a) = g(a) = 0이면 접선은 f(x) ≈ f′(a)(x − a), g(x) ≈ g′(a)(x − a)다. 나누면 (x − a)가 약분되어 f′(a)/g′(a)가 남는다. "직선의 높이 = 기울기 × 떨어진 거리"도 (a, 0)을 지나는 직선이라서 맞다. 이 설명은 g′(a) ≠ 0일 때의 직관이고 엄밀한 증명이 아니다. 대본이 "증명"이라고 하지 않았으므로 통과다(지적 8은 선택 보강).
- **장면 7 (주자 비유):** 두 주자가 시각 T에 동시에 도착하고 결승 직전 속도가 v₁, v₂이면, 남은 거리는 dᵢ ≈ vᵢ(T − t)다. 따라서 d₁/d₂ → v₁/v₂다. 남은 시간이 (x − a), 남은 거리가 f(x), g(x), 속도가 f′, g′에 대응한다. 화면처럼 일정한 속도로 3배 먼 곳에서 3배 빠르게 출발하면 남은 거리는 언제나 3 : 1이다. **맞다.**
- **장면 8 (반례):** x → 0에서 (x+1)/(x+2) → 1/2이다(0/0 아님). 위아래를 미분하면 1/1 = 1이 되어 틀린 값이 나온다. **맞다.** 다만 표현을 지적 5로 다듬는다.
- **장면 9 (정리 진술):** ① 0/0 또는 ∞/∞, ② a 근처에서 미분 가능하고 g′(x) ≠ 0, ③ lim f′/g′ 존재 → lim f/g = lim f′/g′. 표준 진술(Wikipedia의 네 조건)과 일치한다. "a 근처"에서 a 자신은 빼도 된다는 점과 a = ±∞인 경우는 생략했지만, high 모드 영상에서 틀린 말은 아니다(지적 7은 선택 보강).
- **장면 10~11 (예제):** (1³ − 1)/(1 − 1) = 0/0이다. f′ = 3x², g′ = 1이므로 3·1/1 = **3**이다. 인수분해 검산: x² + x + 1 → 3. 수치 검산: x = 1.001이면 (1.003003001 − 1)/0.001 = 3.003. **맞다.** g′ = 1 ≠ 0이라 조건 ②도 충족한다.

## 표현과 인용
- 편지 내용은 따옴표 없이 요지(간접화법)로 쓰고, 화면에도 '요지'로 표기했다. 직접 인용이 없으므로 저작권법 제28조 문제는 없다.
- 대본 문장은 리서치 자료(Wikipedia, MacTutor, 학생 블로그)의 문장을 번역해 옮긴 흔적 없이 새로 썼다. 예제 (x³ − 1)/(x − 1)와 반례 (x+1)/(x+2)는 흔한 수학적 사실이고 특정 교재의 표현이 아니다.
- 참고 블로그 "메르"와 채널 "신비한 건축사전"의 원문은 이번에 직접 대조하지 못했다. 대본에 그 문장이나 고유 인트로, 브랜딩을 가져온 흔적은 없다(위험도 하).
- 특정 기업이나 제품을 비방하는 표현은 없다.

## 지적 사항
| # | 위치(장면/파일) | 문제 | 위험도 | 수정 지시 | 담당 팀 |
|---|---|---|---|---|---|
| 1 | 장면 1 `visual.description` (배경 `study_desk_night`) | AI로 만든 배경 영상인데 AI 표시가 없다. 재현이 아닌 현대 연출 장면이어도 AI 영상마다 표시를 붙여야 한다 | 중 | description 끝에 다음 문장을 추가: "배경 영상에 'AI로 만든 영상' 표시" | 기획팀(구성표), 제작팀(렌더링) |
| 2 | 장면 4 `visual.description` (배경 `noble_study`) | AI 재현 영상인데 AI 표시가 없다 | 중 | description 끝에 다음 문장을 추가: "'AI로 만든 재현 영상' 표시" | 기획팀, 제작팀 |
| 3 | `media` AI 프롬프트 4개 | 1690년대 장면에 시대에 맞지 않는 요소가 끼어들 수 있다(파리 항공 장면의 에펠탑과 19세기 오스만 건물, 실내 전등, 1690년대에 흔하지 않던 봉투) | 하 | 각 프롬프트 끝에 다음을 추가. `paris_1690s`: ", no Eiffel Tower, no 19th-century Haussmann buildings, no street lamps, no cars, no modern bridges" / `noble_study`: ", no electric lights, no modern objects" / `quill_letter`: ", folded letter sheet, no envelope, no modern pen" / `library_dawn`: ", no electric lights, no modern objects". 생성 뒤 2차 검토에서 장면을 확인한다. `quill_letter`는 손만 나오고 얼굴이 없어 실존 인물 재현 기준에 맞는다 | 기획팀(프롬프트), 제작팀 |
| 4 | 장면 4 나레이션 2문장 | "실리면서, 그의 이름으로 불리게 됐습니다"는 1696년 무렵부터 그 이름으로 불렸다는 뜻으로 읽힌다. 이름이 붙은 시점은 리서치에서 확인하지 못했다 | 하 | say: "이 방법은 두 해 뒤 로피탈의 책에 실렸고, 그래서 지금은 그의 이름으로 불립니다." (sub 동일) | 기획팀 |
| 5 | 장면 8 나레이션 3문장 | "(x + 1)/(x + 2)는 1/2인데"는 식 자체가 1/2이라는 뜻으로 읽힌다. 1/2인 것은 극한값이다 | 하 | say: "엑스가 영으로 갈 때, 엑스 더하기 일, 나누기, 엑스 더하기 이의 극한은 이분의 일인데," / sub: "x → 0일 때, (x + 1)/(x + 2)의 극한은 1/2인데," | 기획팀 |
| 6 | 장면 8 `visual.description` | '0/0 아님'에 초록 체크를 붙이면 "로피탈을 써도 된다"는 신호로 오해할 수 있다 | 하 | 해당 부분을 다음으로 교체: "0을 대입하면 1/2 → 정답 1/2에 초록 체크, 옆에 '0/0 아님 → 로피탈 사용 불가' 라벨" | 기획팀, 제작팀 |
| 7 | 장면 10 나레이션 2문장, 장면 11 화면 | "조건이 맞습니다"는 세 조건이 모두 확인된 것처럼 들리는데, 이 시점에 확인한 것은 ①뿐이다 | 하 | 장면 10 say: "일을 넣어 보면 영 나누기 영, 첫 번째 조건이 맞습니다." / sub: "1을 넣어 보면 0/0, 첫 번째 조건이 맞습니다." 장면 11 description에 다음 문장을 추가: "미분 직후 체크리스트 ②(g′(x) = 1 ≠ 0), ③(극한 3 존재)에 체크". (선택) 장면 9 체크리스트 ②에 작은 글씨 "(x = a는 빼도 됨)" | 기획팀, 제작팀 |
| 8 | 장면 6 화면 (선택) | 직관적 설명이 증명처럼 보일 수 있다 | 하 | (선택) description에 다음 문장을 추가: "화면 구석에 작은 글씨 '직관적 설명 · 엄밀한 증명은 코시의 평균값 정리'" | 기획팀 |
| 9 | `media.analyse_title` | 커먼즈 JPG 파일명은 위키백과 미러의 썸네일 주소(`/thumb/2/21/`)로만 보았고, 파일 설명 페이지를 확인하지 못했다. 같은 책의 PDF(`File:Analyse des infiniment petits pour l'intelligence des lignes courbes par Mr le Marquis De l'Hospita.pdf`, 1715년, 퍼블릭 도메인 원본을 기계적으로 스캔한 것)는 미러에서 파일명과 라이선스가 확인된다(파일명 끝 'Hospita'는 실제 파일명이다) | 중 | `fetch_media.py`가 JPG 설명 페이지의 라이선스를 확인하고 `sources.json`에 기록한다. 페이지가 없거나 라이선스가 불명확하면 위 PDF의 속표지 쪽을 쓴다. 어느 쪽이든 화면 캡션 '1715년 판 속표지'는 **반드시** 읽을 수 있는 크기로 넣는다(연표는 '1696'이므로 이 캡션이 없으면 사실과 다른 화면이 된다). 2차 검토 전에 해소할 것 | 제작팀, 기술지원팀 |
| 10 | `media.lhopital_portrait` | 미러 기준 PD-old-70 + Public Domain Mark이고 2005년 독일어 위키백과에서 옮겨 온 파일이다. 원작자와 제작 연도를 커먼즈 페이지에서 확인하지 못했다(Edelinck가 Fouché 그림을 바탕으로 새긴 판화일 가능성이 높으며, Edelinck는 1707년 사망) | 하 | `fetch_media.py` 실행 때 커먼즈 페이지의 작가, 연도, 미국 PD 태그를 `sources.json`에 기록한다. 판화 사진이므로 얼굴을 써도 된다(진본 초상) | 제작팀 |
| 11 | `media.bernoulli_portrait` | 레이크스 미술관 기록상 RP-P-1908-3095는 Heinrich Pfenninger(1759~1815)의 점각 판화이며 퍼블릭 도메인이다. 베르누이 사후에 만든 판화라는 점만 알아 두면 된다 | 하 | `sources.json`에 "Heinrich Pfenninger, Rijksmuseum RP-P-1908-3095, Public Domain(CC0)"으로 기록한다 | 제작팀 |
| 12 | 나레이션 (ElevenLabs) | **사용자 계정 플랜을 모른다.** ElevenLabs 공식 도움말(검색 결과 기준)에 따르면 **무료 플랜에는 상업 라이선스가 없고** 상업적 목적으로 쓸 수 없다. 무료나 비로그인으로 만든 콘텐츠는 제목에 "elevenlabs.io"를 넣어야 한다. **모든 유료 플랜에는 상업 라이선스가 포함된다**(Beta Services 제외). 유료 플랜의 출처 표기는 개별 계약에 따르며, 일반적인 유료 플랜에서는 의무가 아니다. 제3자 자료에 따르면 상업 이용 권리는 **유료 플랜 기간에 생성한 음성**에만 적용된다. 수익화 채널이므로 무료 플랜이면 공개용으로 쓸 수 없다 | 중 (**사용자 확인 필요**) | 나레이션을 생성하기 **전에** 사용자가 유료 플랜(Starter 이상)인지 확인한다. 확인한 플랜 이름과 날짜를 `sources.json`의 TTS 항목에 기록한다. 무료 플랜이면 공개용 음성을 만들지 말고 총괄 PD에게 보고한다 | 사용자, 제작팀 |
| 13 | 나레이션 목소리 "Jae - Calm Korean Narrator" (라이브러리 professional voice, `1wnzzdVjmRUxpiionYOT`) | 라이브러리 보이스는 소유자가 공유를 중단할 수 있다. 공지 기간(notice period)이 있으면 그 기간 동안만 계속 쓸 수 있고, 없으면 공유를 중단하는 즉시 접근이 끊긴다. 라이브러리 보이스의 상업적 이용을 따로 제한하는 공식 문구는 찾지 못했다(일반 약관과 플랜 조건을 따르는 것으로 판단). 실존 인물의 목소리를 사칭하는 용도가 아니므로 정책 위반 요소는 없다 | 하 (**사용자 확인 필요**) | 목소리를 My Voices에 저장하고, 보이스 카드의 공지 기간과 사용 조건(상업 이용 제한 표시가 있는지)을 화면으로 확인해 `sources.json`에 기록한다 | 제작팀 |
| 14 | TTS 모델 `eleven_v4` | 보도에 따르면 2026-09-28에 정식 출시되었고 베타나 알파 표시는 없다. 공식 페이지는 열지 못했다. 상업 라이선스는 Beta Services를 제외하므로 확인이 필요하다 | 하 | 생성 화면이나 모델 목록에서 eleven_v4에 Beta/Alpha 표시가 없는지 확인하고 기록한다. 표시가 있으면 정식 모델로 바꾼다 | 제작팀 |
| 15 | AI 영상 생성 (Higgsfield) | Higgsfield 도움말(검색 결과 기준, 이용약관 4.4항)에 따르면 생성물의 소유권은 이용자에게 있고 **모든 이용자**가 상업적으로 쓸 수 있다. 다만 일부 플랜은 생성물에 워터마크가 박힌다. 약관 원문은 열지 못했다 | 중 (**사용자 확인 필요**) | 생성하기 전에 사용 플랜을 확인하고 워터마크 없는 유료 플랜에서 만든다. 플랜 이름과 생성 날짜를 `sources.json`에 기록한다 | 사용자, 제작팀 |
| 16 | `.claude/agents/legal-reviewer.md` 48행 | 법무팀 지침의 "나레이션 음성" 항목이 아직 CLOVA Voice 기준이다. 현재 기본 엔진은 ElevenLabs다(`CLAUDE.md`, `scripts/tts.py`) | 하 | 지침을 "기본 TTS(ElevenLabs, 예비 CLOVA Voice)의 상업적 이용·출처 표기 조건 확인"으로 바꿀지 사용자 승인을 받는다(법무팀은 설정 파일을 직접 고치지 않는다) | 총괄 PD |

- 지적 4~7을 반영하면 나레이션이 약 10~15자 늘어난다. 1,200자 상한 안에 드는지 `storyboard_to_script.py`로 다시 확인할 것.

## 자료 계획 (`source_hint`/`media`)
- AI 영상 5개: Higgsfield로 생성한다. 프롬프트에 "no recognizable real person"과 "no text"가 들어 있고, 실존 인물은 손(`quill_letter`)만 나온다. 기준에 맞는다(지적 1~3, 15 조건).
- 커먼즈 3개: 모두 사용 가능한 유형(17~18세기 판화, 옛 책 스캔. 퍼블릭 도메인)이다(지적 9~11 조건).
- 1696년 초판 속표지 사진(MAA, 에드워드 워스 도서관)은 재사용 조건을 확인하지 못해 쓰지 않기로 한 판단이 적절하다.
- 나머지 장면은 자체 제작 애니메이션이라 통과다.

## 나레이션 음성 확인 결과 (ElevenLabs)
- 서비스: ElevenLabs, 모델 `eleven_v4`, 목소리 "Jae - Calm Korean Narrator"(라이브러리 professional voice)
- 상업적 이용: 유료 플랜이면 가능하고(Beta 제외), 무료 플랜이면 불가하다. **사용자 플랜 미확인 → 사용자 확인 필요**
- 출처 표기: 무료 플랜은 제목에 "elevenlabs.io"를 넣어야 한다. 유료 플랜은 개별 계약에 따르며 일반적으로 의무가 아니다.
- 확인 방법: 웹 검색 결과에 나온 ElevenLabs 공식 도움말 "Can I publish the content I generate on the platform?" 요약과 Voice Library 문서 요약. **elevenlabs.io 원문 미열람**(세션 네트워크에서 차단). 원문을 확인하려면 세션 허용 도메인에 elevenlabs.io를 추가해야 한다.

## 유통팀 전달 사항
- **AI 합성 콘텐츠 공개 필요 여부:** **켠다.** 사실적인 AI 영상(1690년대 파리 항공 장면, 귀족 서재, 깃펜으로 편지 쓰는 손, 옛 도서관, 공부하는 학생 책상)이 실제 역사 기록 영상처럼 보일 수 있다. 화면 안 'AI로 만든 (재현) 영상' 표시와 별개로, 유튜브 업로드 시 "변경되거나 합성된 콘텐츠"를 "예"로 설정한다. 합성 음성 나레이션은 특정 실존 인물을 흉내 내는 것이 아니므로 그것만으로는 공개 대상이 아니다. 업로드 시점의 정책은 다시 확인한다.
- **아동용 설정 의견:** **"아동용 아님".** 대상이 고등학생 이상이고(난이도 high, 대학 미적분 내용), 아동을 겨냥한 캐릭터나 놀이 요소가 없다.
- **설명란에 넣어야 할 출처와 라이선스 표기:**
  - 이미지: "로피탈 후작 초상: 위키미디어 커먼즈, 퍼블릭 도메인" / "요한 베르누이 초상: Heinrich Pfenninger 판화, 레이크스 미술관 RP-P-1908-3095, 퍼블릭 도메인" / "『무한소 해석』 1715년 판 속표지: 위키미디어 커먼즈, 퍼블릭 도메인"(2차 검토 때 확정한 파일명과 원작자로 바꿔 적는다)
  - 영상: "역사 장면 일부는 AI로 만든 재현 영상입니다(Higgsfield)."
  - 나레이션: 유료 플랜이면 표기 의무는 없다. 무료 플랜이면 공개하지 않는다(지적 12).
  - 참고 자료: MacTutor History of Mathematics(로피탈 전기, 1694년 3월 17일 편지 번역, 『무한소 해석』 머리말 번역), Bradley·Petrilli·Sandifer, *L'Hôpital's Analyse des infiniments petits*(Springer, 2015), Wikipedia "L'Hôpital's rule", Harvard(Knill) "The agreement of Bernoulli with de l'Hôpital"
- **제목:** "로피탈의 정리: 0/0은 빠르기 대결이다"는 내용과 일치하며 낚시성 표현이 아니다. 썸네일에서 "로피탈이 훔쳤다"처럼 단정하는 문구는 쓰지 않는다(2차 검토에서 확인).

## 참고한 웹 자료 (검색 결과로 확인)
- MacTutor: 3월 17일 편지 https://mathshistory.st-andrews.ac.uk/Miscellaneous/messages/03-17 , 머리말 https://mathshistory.st-andrews.ac.uk/Extras/LHopital_Preface (원문 미열람)
- College Board AP 자료 https://secure-media.collegeboard.org/apc/ap08_calc_LHospital_final.rev1.pdf (원문 미열람)
- Springer 역주본 12장 https://rd.springer.com/chapter/10.1007/978-3-319-17115-9_12 (원문 미열람)
- Wikipedia: Guillaume de l'Hôpital https://en.wikipedia.org/wiki/Guillaume_de_l%27H%C3%B4pital , Analyse des infiniment petits https://en.wikipedia.org/wiki/Analyse_des_infiniment_petits_pour_l%27intelligence_des_lignes_courbes
- Harvard(Knill) https://people.math.harvard.edu/~knill/teaching/math1a_2011/exhibits/bernoulli/index.html
- 레이크스 미술관 RP-P-1908-3095 https://www.rijksmuseum.nl/en/collection/object/Portret-van-Johann-Bernoulli-I--5dfcaa3696546498742730e6f1e5908a
- 커먼즈 미러: https://download.osmand.net/wiki/File:Guillaume_de_l%27H%C3%B4pital.jpg , https://download.osmand.net/wiki/File:Analyse_des_infiniment_petits_pour_l%27intelligence_des_lignes_courbes_par_Mr_le_Marquis_De_l%27Hospita.pdf
- ElevenLabs 도움말 https://elevenlabs.io/docs/help-center/legal/can-i-publish-the-content-i-generate-on-the-platform , Voice Library https://elevenlabs.io/docs/voices/voice-library/overview , v4 소개 https://elevenlabs.io/de/v4 (모두 원문 미열람)
- Higgsfield 도움말 https://higgsfield.ai/creator-hub/help-center/account/who-owns-my-generations-and-can-i-use-them-commercially (원문 미열람)

---

## 총괄 PD 반영 기록 (2026-10-29)
- 수정 지시 1~8 반영: 장면 1·4 AI 표시, 프롬프트 4개 시대 고증 문구, 장면 4·8·10 문장 수정, 장면 6 '직관적 설명' 표기, 장면 8 체크·라벨, 장면 11 조건 ②③ 체크. 수정 후 나레이션 1,181자.
- 리서치 노트 강의록 발견 연도 "1921년(자료에 따라 1922년)"으로 수정.
- 지적 16: `legal-reviewer.md`의 나레이션 기준을 ElevenLabs로 갱신(사용자가 이번 요청에서 ElevenLabs를 지정함).
- **지적 12 확인 결과: 사용자 ElevenLabs 계정은 무료 플랜이다.** 생성 도중 "비정상 활동 감지로 무료 플랜 사용 중지" 오류가 나 12개 중 5개 장면이 실패했다(`assets/audio/elevenlabs/manifest.json`). 무료 플랜 생성분은 상업 라이선스가 없으므로 **현재 음성으로는 공개 불가**. 유료 플랜 전환 후 12개 장면을 모두 다시 생성해야 한다.
- 발음 점검(받은 7개 장면, 27문장): 평균 CER 0.178. 오류 상당수는 음성 인식기가 고유명사(로피탈, 베르누이, 리브르)를 모르는 데서 생긴 것으로 보이며, 공개 전 기준(10% 미만)은 재생성분으로 다시 확인한다.
