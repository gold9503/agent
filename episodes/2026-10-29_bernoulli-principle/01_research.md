# 리서치 노트: 베르누이의 원리

## 0. 최우선 다섯 줄 (대본보다 먼저 정함)

1. **훅 (첫 5초):** 종이 두 장 사이로 숨을 세게 불면, 밀려나야 할 종이가 오히려 서로 달라붙는다. ("바람이 밀었는데, 왜 다가올까요?")
2. **핵심 비유 하나:** 흐르는 물 한 덩어리는 **총액이 정해진 지갑**을 들고 다닌다. 주머니는 셋: 미는 주머니(압력), 달리는 주머니(움직임의 에너지), 높이 주머니(높이의 에너지). 빨리 달리려면 미는 주머니에서 꺼내 써야 한다. 이 비유 하나로 훅, 다니엘의 유리관, 벤투리관, 날개, 공식, 예제까지 끝까지 민다.
3. **"아하!" 순간 (약 1:15~1:35):** 투명한 관에서 물이 좁은 곳으로 들어서며 빨라지는 순간, 그 위 유리관의 물기둥이 쑥 내려간다. "빨라진 만큼 미는 힘을 써 버린 것". 그래서 종이 사이 공기도 덜 밀고, 바깥 공기가 종이를 안으로 민다. 첫 장면의 수수께끼가 여기서 풀린다.
4. **깨뜨릴 오해:** "날개 위쪽 길이 더 길어서, 위아래 공기가 뒤끝에서 동시에 만나려면 위쪽이 빨라야 한다"(같은 시간 도착설)는 틀렸다. 실제로는 위쪽 공기가 훨씬 먼저 도착한다. 날개는 공기를 아래로 꺾어 내리고(뉴턴 제3법칙) 그와 동시에 날개 위 압력이 낮아진다(베르누이). 둘은 같은 흐름의 두 얼굴이다.
5. **마지막 한 방:** "빨리 달리는 공기는, 덜 밉니다. 여러분 입김이 종이를 붙인 그 원리가, 오늘도 하늘에서 여객기를 받칩니다."

---

- **난이도 모드:** `univ`(대학 유체역학 · 베르누이 방정식). 단, 사용자 지시에 따라 **중학생이 한 번 듣고 이해하는 수준**으로 쓴다. 공식은 말로 먼저("압력 더하기 움직임의 에너지 더하기 높이의 에너지는 늘 일정"), 기호는 화면에만.
- **교육과정 위치:** 대학 유체역학(공학 기초) 개념이다. 한국 고교 교육과정(2015 개정 물리학Ⅱ, 2022 개정 '역학과 에너지')에 베르누이 법칙이 성취기준으로 들어 있는지는 **이번 리서치에서 확인하지 못했다.** 검색으로 교육과정 원문(ncic)에 도달하지 못함. 화면과 설명란에 "고교 교육과정 ○○ 단원" 같은 표기는 하지 않는다.
  - 참고(확인 실패 기록): [2007~2022 개정 고등학교 물리학 교육과정의 성취기준 특징 분석 (조선대)](https://oak.chosun.ac.kr/handle/2020.oak/17709) — 베르누이 포함 여부 언급 없음.
- **나레이터:** 신뢰감 있는 중후한 남성 다큐 목소리(ElevenLabs).
- **조사 환경 메모:** 이번 세션에서 `en.wikipedia.org`, `mathshistory.st-andrews.ac.uk`가 네트워크에서 차단되어 원문 페이지를 직접 열지 못했다. 아래 출처는 **웹 검색 결과 요약으로 확인한 것**이며, 법무팀 검토 때 원문 대조가 필요하다(특히 ★ 표시).

## 1. 정의

정상류(시간에 따라 흐름이 변하지 않음), 비압축성(밀도 일정), 점성(마찰) 무시 조건에서 **같은 유선(흐름선)을 따라** 다음이 일정하다.

> P + ½ρv² + ρgh = 일정

| 기호 | 뜻 | 단위 | 영상에서 쓰는 말 |
|---|---|---|---|
| P | 정압(유체가 옆으로 미는 압력) | Pa (= N/m² = J/m³) | 압력, 미는 주머니 |
| ½ρv² | 단위 부피당 운동 에너지(동압) | Pa | 움직임의 에너지, 달리는 주머니 |
| ρgh | 단위 부피당 위치 에너지 | Pa | 높이의 에너지, 높이 주머니 |
| ρ | 밀도 (물 약 1000 kg/m³, 공기 약 1.2 kg/m³) | kg/m³ | 밀도 |
| v | 유속 | m/s | 속력 |
| h | 기준면으로부터 높이 | m | 높이 |

- 핵심 문장: **흐름이 빨라지는 곳에서는 압력이 낮아진다.** 본질은 에너지 보존이다. 다니엘 베르누이의 『유체역학』은 하위헌스 계열의 활력(vis viva) 보존을 바탕으로, 움직이는 유체가 운동 에너지와 압력을 맞바꾼다는 생각을 담았다.
  - 출처: [Hydrodynamica (Wikipedia, 검색 요약)](https://en.wikipedia.org/wiki/Hydrodynamica) ★, [Encyclopedia.com: Bernoulli, Daniel](https://www.encyclopedia.com/science/encyclopedias-almanacs-transcripts-and-maps/daniel-bernoulli) ("a moving fluid traded its kinetic energy for pressure", 빨라지면 옆으로 미는 압력이 줄어든다), [Ian Bruce 역 Hydrodynamica 12장](https://17centurymaths.com/contents/danielbernoulli/hydrodynamics12.pdf) (12장 정리는 "물의 위치·운동 에너지 총합 보존"에 관한 것, 유선 개념은 뒤에 오일러가 보탬). 신뢰도: 상
- 대본의 "정확히는" 한 줄: "마찰 없이 한 줄기로 고르게 흐를 때의 이야기" = 점성 무시 + 같은 유선 + 정상류. (비압축성은 물과 저속 공기에서 근사적으로 성립. 대본에서는 생략)

## 2. 역사

| 시기 | 내용 | 신뢰도 | 출처 |
|---|---|---|---|
| 1700 | 다니엘 베르누이, 네덜란드 흐로닝언 출생. 아버지는 요한 베르누이(지난 편 로피탈의 정리에서 로피탈에게 미분을 가르친 인물). **생일은 자료마다 1월 29일 / 2월 8일로 갈린다**(율리우스력·그레고리력 차이로 추정). 대본에는 연도도 쓰지 않음. 화면 이름 카드에 "1700~1782"만. | 상(연도) / 중(날짜) | [APS News: This Month in Physics History](https://www.aps.org/apsnews/2020/01/birth-daniel-bernoulli-1700) (1월 29일), [EBSCO Research Starters](https://www.ebsco.com/research-starters/history/daniel-bernoulli-and-energy-conservation) (2월 8일), [Gran Enciclopèdia Catalana](https://www.enciclopedia.cat/EC-GEC-0009528) |
| 1782 | 바젤에서 사망. | 상 | [MacTutor 전기(검색 요약)](https://mathshistory.st-andrews.ac.uk/Biographies/Bernoulli_Daniel/) ★ |
| 1725~1733 | 상트페테르부르크 아카데미에서 활동. 1726년 오일러가 뒤따라 옴. 『유체역학』은 "1733/1738"로 표기되기도 한다(페테르부르크 시절 대부분 집필). 대본에서 쓰지 않음. | 중상 | [EPS Historic Site: Stachelschützenhaus](https://members.eps.org/blogpost/751263/492786/The-Stachelschutzenhaus-will-be-inaugurated-as-an-EPS-Historic-Site-in-September-2023-in-Basel-Switzerland) |
| **1734** | 파리 왕립 과학 아카데미 대상(행성 궤도 문제)을 **다니엘과 요한이 공동 수상**. 아들과 동급으로 평가받은 데 화가 난 요한이 **다니엘을 바젤 집에서 내쫓았다(banned him from the house)**. 대본은 "~다고 전해집니다"로 쓴다. | 중상 | [MacTutor 전기(검색 요약)](https://mathshistory.st-andrews.ac.uk/Biographies/Bernoulli_Daniel/) ★, [APS News](https://www.aps.org/apsnews/2020/01/birth-daniel-bernoulli-1700) ("furious, banning his son from his house"), [AAAS Scientia: Bernoulli succeeded despite paternal rivalry](https://www.aaas.org/blog/scientia/bernoulli-succeeded-despite-paternal-rivalry) |
| **1738** | 『유체역학(Hydrodynamica, sive de Viribus et Motibus Fluidorum Commentarii)』 스트라스부르 출간. "hydrodynamics"라는 말도 다니엘이 만들었다. | 상 | [Hydrodynamica (Wikipedia, 검색 요약)](https://en.wikipedia.org/wiki/Hydrodynamica) ★, [Linda Hall Library: Scientist of the Day](https://www.lindahall.org/about/news/scientist-of-the-day/daniel-bernoulli/) |
| 1739 또는 1743 (표기 1732) | 요한의 『수력학(Hydraulica)』. 책에는 **1732년**으로 적혀 있으나 실제 출간은 더 늦다. 실제 연도는 **1743(Wikipedia) / 1739(bookofproofs 등)**로 갈린다. 아들의 발견을 자기 것처럼 앞선 날짜를 붙였다는 평가가 일반적이나, "다니엘 주장만큼 단순하지 않다"는 견해도 있다. **대본은 "더 이른 연도를 적었다는 의심을 받죠"로만 쓰고 실제 연도는 말하지 않는다.** | 중상(앞당긴 표기) / 중(실제 연도) | [Hydrodynamica (Wikipedia, 검색 요약)](https://en.wikipedia.org/wiki/Hydrodynamica) ★, [bookofproofs: Bernoulli, Daniel](https://bookofproofs.github.io/history/18th-century/bernoulli-daniel.html), [Encyclopedia.com](https://www.encyclopedia.com/history/encyclopedias-almanacs-transcripts-and-maps/daniel-bernoulli) |
| 1752 / 1755(1757 간행) | 오일러가 유체 운동의 일반 방정식(연속 방정식, 운동량 방정식)을 세웠고, 오늘날의 미분 형태 베르누이 방정식은 이 틀에서 나온다. **"오일러가 몇 년에 현대식 베르누이 식을 처음 썼다"는 정확한 연도는 확인 못 함 → 대본에 쓰지 않음.** | 중 | [Darrigol & Frisch (OCA)](https://www.oca.eu/etc7/EE250/texts/darrigol-frisch.pdf), [U.S. Centennial of Flight: Euler](https://centennialofflight.net/essay/Dictionary/Euler/DI144.htm) |

### 다니엘의 압력 측정 (유리관)
- 다니엘은 **관 벽에 구멍을 뚫고 끝이 열린 가는 관을 꽂아**, 그 관에 액체가 올라간 높이로 압력을 쟀다. 출처: [Plus Magazine (Cambridge): Daniel Bernoulli and the making of the fluid equation](https://plus.maths.org/issue1/bern/index.html) ("puncturing the wall of a pipe with a small open ended straw"). 신뢰도: 중상(대중 과학지)
- 대본 문장 "물이 빨리 흐르는 곳에선, 물기둥이 오히려 낮았습니다"는 위 측정법 + 『유체역학』의 결론(빨라지면 옆으로 미는 압력 감소, Encyclopedia.com)을 합친 서술이다. 다니엘이 **특정 실험에서 그 장면을 정확히 봤다는 1차 사료는 확인하지 못했다.** ★ 법무팀 확인 항목.

### 쓰지 않기로 한 것 (의학 연결)
- "유럽 의사들이 다니엘의 방법으로 동맥에 유리관을 꽂아 혈압을 쟀다"는 이야기가 Plus Magazine, Encyclopedia.com, AAAS 글에 있다. 그런데 **사용 기간이 자료마다 '100년 이상 / 약 170년 / 거의 200년'으로 다르고**, 동맥에 관을 꽂아 혈압을 처음 잰 사람은 **스티븐 헤일스(말 실험, 『Haemastaticks』 1733)**로 더 일찍이다. 다니엘의 방법이 의학의 출발점처럼 들릴 위험이 있어 **대본에서 뺐다.**
  - 출처: [Plus Magazine](https://plus.maths.org/issue1/bern/index.html), [AAAS Scientia](https://www.aaas.org/blog/scientia/bernoulli-succeeded-despite-paternal-rivalry), [Pumps & Systems: The Life and Work of Daniel Bernoulli](https://www.pumpsandsystems.com/life-and-work-daniel-bernoulli), [Wood Library-Museum: Hales 1733 Haemastaticks](https://www.woodlibrarymuseum.org/wp-content/uploads/reflections/048_Hales_1733_Haemastaticks_Bause_GS.pdf), [RCPE: Blood Pressure in the College Collections](https://www.rcpe.ac.uk/heritage/blood-pressure-college-collections)

**대본 반영 원칙**
- 쓰는 사실: 요한의 아들(지난 편 "숨은 스승" 연결), 1734년 파리 아카데미 공동 수상과 집에서 내쫓김("전해집니다"), 1738년 『유체역학』, 아버지 책의 앞당긴 연도("의심을 받죠"), 관 벽에 꽂은 유리관으로 압력 측정.
- 쓰지 않는 것: 생일, 상트페테르부르크, 혈압 측정, 오일러 연도, 『수력학』 실제 출간 연도.

## 3. 개념의 탄생 흐름 (영상 ③구간)

1. 질문: 흐르는 물은 관 벽을 얼마나 세게 미는가? 고여 있는 물이라면 깊이만 알면 되지만, 흐르는 물은?
2. 측정: 관 벽에 꽂은 유리관의 물기둥 높이 = 그 자리의 압력(ρgh로 환산되는 눈금).
3. 관찰과 생각: 관이 좁아져 물이 빨라지는 곳에서는 물기둥이 낮다. 물이 얻은 "움직임"은 어디서 왔나? → 미는 힘(압력)에서 왔다.
4. 일반화: 활력(운동 에너지) 보존 사고를 유체에 적용 → 압력, 운동, 높이의 몫을 합친 것이 일정.
- 출처: 위 2절 Encyclopedia.com, Ian Bruce 역, Plus Magazine.
- 영상에서는 3번을 **지갑 비유**로 바꾸고, 현대 벤투리관 실연 영상으로 "아하"를 만든다. (벤투리관 자체는 19세기 이후 이름이 붙은 장치라 **"다니엘의 실험"이라고 부르지 않는다.** 화면 표기 "오늘날의 실험 장치")

## 4. 훅 실험 선택 근거

| 후보 | 판단 | 근거 |
|---|---|---|
| **종이 두 장 사이로 불기** | **채택.** 집에서 바로 되고, 결과(달라붙음)가 확실하다. 파인먼 강의(제2권 40장)와 시드니대 물리 실습 자료가 "좁은 틈의 빠른 공기 → 압력이 대기압보다 낮음 → 바깥 공기가 종이를 민다"로 설명한다. | [U. Sydney: Two Sheets of Paper](https://www.physics.usyd.edu.au/super/physics_tut/activities/Properties_of_Matter/Two_Sheets_of_Paper.pdf), [UBA 강의 블로그(파인먼 인용)](https://materias.df.uba.ar/edlm1a2022c2/bernoulli-soplando-papeles) |
| ⚠️ 위 설명에 대한 반론 | 일부 교육자는 "자유 제트는 대기압과 같다", "코안다 효과·경계층이 섞인다"며 단순 베르누이 설명을 비판한다(UMD 강의 시연 포럼: 한 장만 매달아도 안쪽으로 온다). 반면 **두 장을 3~5cm 간격으로 나란히 두면 좁은 통로의 압력 강하가 뚜렷하다**는 견해도 있다. 대본은 "좁은 틈을 빨리 지나느라 덜 밀고"로 **좁은 통로**를 강조해 파인먼식 설명 범위에 머문다. | [NSTA: Is it really caused by the Bernoulli effect?](https://www.nsta.org/q-it-really-caused-bernoulli-effect), [UMD Lecture Demo F5-03](https://lecdem.physics.umd.edu/forum/f5/563-f5-03-thin-metal-sheets-coanda-effect.html), [JSME 유체 실험](https://jsme-fed.org/experiment-e/2011_10/002.html), [boatdesign.net 토론](https://www.boatdesign.net/goto/post?id=686599), [Eastwell, Science Education Review](https://eclass.upatras.gr/modules/document/file.php/PN1483/THE%20SCIENCE%20EDUCATION%20REVIEW/ser_6_1.pdf) |
| 드라이어 위 탁구공 | 제외. 공이 떠 있는 이유(안정성)에 코안다 효과·제트 곡률 설명이 섞여 논쟁적. | NSTA 위 자료 |
| 수돗물 줄기와 숟가락 | 제외. 코안다 효과가 주원인. | 기획 지시 |
| 종이 한 장 위로 불기(종이가 떠오름) | 제외. 유선 곡률·코안다로 설명하는 쪽이 정확하다는 비판이 강함. | [Eastwell](https://eclass.upatras.gr/modules/document/file.php/PN1483/THE%20SCIENCE%20EDUCATION%20REVIEW/ser_6_1.pdf), [NSTA](https://www.nsta.org/q-it-really-caused-bernoulli-effect) |

## 5. 흔한 오해

1. **같은 시간 도착설(대본에서 깨뜨림):** "날개 위 길이 더 길어서 위아래 공기가 뒤끝에서 동시에 만나야 하므로 위가 빠르다." → 틀림. NASA 글렌 연구소: 실제 윗면 속도는 '동시 도착'이 요구하는 속도보다 훨씬 빠르고, 윗면 공기가 뒤끝에 **먼저** 도착한다. 이 이론으로 계산한 양력은 실제보다 훨씬 작다. 대칭 날개, 평판, 종이비행기, 배면 비행도 설명 못 한다. 케임브리지대 바빈스키의 연기 펄스 영상(2012)에서도 위쪽 연기가 뒤끝을 먼저 지난다.
   - 출처: [NASA Glenn: Incorrect Lift Theory (Longer Path)](https://www.grc.nasa.gov/WWW/k-12/VirtualAero/BottleRocket/airplane/bernnew.html) (검색 요약으로 확인 ★), [AVweb: Theories of Lift](https://avweb.com/features/theories-of-lift/), [Babinsky, "How do wings work?", Physics Education 38(6), 497–503, 2003](https://www3.eng.cam.ac.uk/outreach/Project-resources/Wind-turbine/howwingswork.pdf), [Gizmodo: Clever 1-minute video shows how airplane wings really work (2012)](https://gizmodo.com/clever-1-minute-video-shows-how-airplane-wings-really-w-5878773), [phys.org 2012](https://phys.org/news/2012-01-wings.pdf). 신뢰도: 상
2. **"베르누이냐 뉴턴이냐" 양자택일:** NASA 글렌은 압력(베르누이)으로 적분하든 운동량 변화(뉴턴)로 계산하든 같은 공기력이 나오며 **둘 다 맞다**고 쓴다. 날개가 흐름을 아래로 꺾으면(뉴턴 제3법칙의 반작용) 그 흐름 속에서 윗면 압력이 낮고 아랫면 압력이 높아진다. 대본은 "같은 흐름의 두 얼굴"로 표현한다("완전히 동일한 이론"이라는 단정은 피함).
   - 출처: [NASA Glenn: Bernoulli and Newton](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/bernoulli-and-newton), [HyperPhysics: Bernoulli or Newton's Laws for Lift?](https://hyperphysics.gsu.edu/hbase/Fluids/airfoil.html). 신뢰도: 상
3. **"움직이는 공기는 언제나 주변보다 압력이 낮다":** 베르누이는 **같은 흐름선 위에서** 성립한다. 탁 트인 곳으로 뿜어진 자유 제트의 압력은 대략 주변 대기압과 같다. 그래서 대본은 "좁은 틈", "한 줄기로 고르게 흐를 때"라는 단서를 붙인다.
   - 출처: [NSTA](https://www.nsta.org/q-it-really-caused-bernoulli-effect), [Eastwell](https://eclass.upatras.gr/modules/document/file.php/PN1483/THE%20SCIENCE%20EDUCATION%20REVIEW/ser_6_1.pdf). 신뢰도: 상

## 6. 예제 (대본 채택)

수평 관(높이 변화 없음, ρgh 주머니 그대로), 물 ρ = 1000 kg/m³.
- 넓은 곳: v₁ = 1 m/s. 단면적이 절반인 곳: 같은 양의 물이 지나가야 하므로 v₂ = 2 m/s (연속 방정식 A₁v₁ = A₂v₂ — 다음 편 예고 주제).
- 움직임의 에너지: ½ × 1000 × 1² = **500 Pa** → ½ × 1000 × 2² = **2000 Pa** (속력 2배 → 4배). 늘어난 몫 **1500 Pa**.
- 총액 일정 → 압력 P₁ − P₂ = **1500 Pa** 감소.
- 체감: 유리관 물기둥 높이로 환산 h = ΔP/(ρg) = 1500 / (1000 × 9.8) ≈ **0.153 m ≈ 15 cm**.
- 검산: 1500 / 9800 = 0.1531. ✔
- 단순화 메모: 점성 손실 무시. 실제 벤투리관에서는 출구 쪽 물기둥이 입구보다 조금 낮다(마찰 손실). AI 영상 프롬프트에도 반영.

(예비 예제, 채택 안 함) 날개 위 70 m/s, 아래 60 m/s, 공기 ρ ≈ 1.2 → ΔP = 0.6 × (4900 − 3600) = 780 Pa. 오해 구간과 겹쳐 "속도 차가 원인"처럼 들릴 수 있어 제외.

## 7. 일상 연결 검토

| 소재 | 판단 |
|---|---|
| 비행기 | 채택(오해 깨기와 마지막 한 방). |
| 분무기·향수병 | 고무공식 분무기는 벤투리 원리로 설명된다([Sciencing](https://sciencing.com/perfume-atomizer-work-4568884.html), [UQ Physics Museum](https://physicsmuseum.uq.edu.au/node/16444)). 다만 요즘 펌프식 향수병은 원리가 다르고 1차 자료가 약해 **분량상 제외.** |
| 고속열차·트럭 옆 끌림 | 정확한 1차 자료 미확보 → **제외.** |
| 샤워 커튼 | 원인 논쟁 → **제외(지시대로).** |

## 8. 대본 자기 점검
- 중학생이 한 번 듣고 따라오는가: "압력"은 처음부터 "미는 힘"으로 부르고, 공식은 지갑 → 말 → 기호 순서. 파스칼은 화면에 "압력의 단위"로 붙인다.
- 한 문장 = 한 그림: 각 문장에 대응하는 화면을 03_storyboard.json `visual.description`에 적었다.
- 20초마다 궁금증: "왜 다가올까요?"(0:10) → "아들보다 먼저인 척?"(0:45) → "빠른 곳 물기둥이 왜 낮지?"(1:05) → "그럴듯하죠? 하지만 틀렸습니다"(1:55) → "총액은 그대로니까?"(2:35).
- 호칭 "여러분": 1회(마지막 한 방). 오프닝은 명령형 "불어 보세요"로 직접 실험을 부른다.
