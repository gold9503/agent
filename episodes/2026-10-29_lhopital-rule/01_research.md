# 리서치 노트: 로피탈의 정리

- **난이도 모드:** `high` (고등학교 미적분 수강생)
- **교육과정 위치:** 로피탈의 정리는 **한국 고등학교 교육과정에 없다.** 대학 미적분학(부정형의 극한) 내용이다.
  - 선수 개념은 고교 과정에 있다. 2022 개정 교육과정 기준으로 함수의 극한, 미분계수, 도함수는 일반 선택 과목 **미적분Ⅰ**에서 다루고, 삼각·지수함수의 미분은 진로 선택 과목 **미적분Ⅱ**에서 다룬다. 2026년 고3은 2015 개정(수학Ⅱ, 미적분)을 적용받는다.
    - 과목 구조 출처: [2022 개정 교육과정 수학 과목 총정리 (geteduify)](https://geteduify.com/education-policy/2022-%ea%b0%9c%ec%a0%95-%ea%b5%90%ec%9c%a1%ea%b3%bc%ec%a0%95-%ec%88%98%ed%95%99-%ea%b3%bc%eb%aa%a9-%ec%b4%9d%ec%a0%95%eb%a6%ac-%ea%b3%b5%ed%86%b5%c2%b7%ec%84%a0%ed%83%9d%c2%b7%ec%88%98%eb%8a%a5/) (2차 자료)
    - ⚠️ 성취기준 원문(교육부 고시, ncic.go.kr)은 이번 리서치에서 직접 확인하지 못했다. 함수의 극한 단원이 미적분Ⅰ의 어느 단원에 있는지는 고시 원문으로 확인해야 한다.
  - 학생들 사이에서는 "교육과정 밖이지만 검산이나 객관식에서 공식처럼 쓰는 도구"로 통한다. 증명이 고교 수준을 넘는다는 인식도 있다. 출처: [틀을 깨는 기발한 수학 (omath 블로그)](https://omath.tistory.com/47), [진학사 탐구 보고서 사례](https://www.jinhak.com/jh/high12/performance/subject-search/3302) (둘 다 2차 자료이며, 학생 인식을 보여주는 용도로만 쓴다)

## 1. 정의 (정리 진술)

열린 구간에서 함수 f, g가 a 근처(a 자신은 제외해도 됨)에서 미분 가능하고, 그 근처에서 g′(x) ≠ 0이라고 하자.

1. lim_{x→a} f(x) = lim_{x→a} g(x) = 0 **또는** 둘 다 ±∞ (부정형 0/0 또는 ∞/∞)
2. lim_{x→a} f′(x)/g′(x) = L 이 존재한다 (L은 실수 또는 ±∞)

그러면 lim_{x→a} f(x)/g(x) = L 이다. (a = ±∞인 경우나 한쪽 극한에도 성립한다.)

- 출처: [L'Hôpital's rule (Wikipedia)](https://en.wikipedia.org/wiki/L%27H%C3%B4pital%27s_rule): 네 조건(부정형, 미분 가능성, 분모 도함수 ≠ 0, 도함수 비의 극한 존재)을 나열하고 "조건 중 하나라도 어기면 일반적으로 성립하지 않는다"고 쓴다. 신뢰도: 상 (표준 교재 내용과 일치)

**기호의 의미**
| 기호 | 뜻 | 영상에서 쓰는 말 |
|---|---|---|
| f(x), g(x) | 분자와 분모 함수 | 분자, 분모 |
| x → a | x가 a에 한없이 가까워짐 | 엑스가 에이로 갈 때 |
| f′(x), g′(x) | 각 함수의 도함수(순간 변화율, 기울기) | 빠르기, 기울기 |
| f′/g′ | 도함수끼리의 비. 몫의 미분 (f/g)′ 와는 **다른 것** | 도함수끼리 나눈 것 |

## 2. 역사

| 시기 | 내용 | 신뢰도 | 출처 |
|---|---|---|---|
| 1661~1704 | 기욤 프랑수아 앙투안 드 로피탈 후작. 파리 태생의 귀족, 기병 장교 출신. 1704년 2월 2일 파리에서 사망. | 상 | [Wikipedia: Guillaume de l'Hôpital](https://en.wikipedia.org/wiki/Guillaume_de_l%27H%C3%B4pital), [MacTutor 전기](https://mathshistory.st-andrews.ac.uk/Biographies/De_LHopital/) |
| (군 은퇴 이유) | 근시(열 걸음 밖이 안 보일 정도) 때문이라는 설명과, 수학을 하고 싶어서가 주된 이유라는 설명(MacTutor)이 섞여 있다. **대본에서 쓰지 않는다.** | 중 | 위 두 자료 |
| 1691년 말(또는 1692년) | 요한 베르누이(1667~1748, 스위스 바젤 출신)가 파리에 와서 말브랑슈 모임에서 강의하다 로피탈을 만난다. 로피탈은 그를 고용해 개인 수업을 받고, 이후 자기 영지 우크(Oucques)에서도 수업을 받는다. 만난 해(1691/1692)와 우크 체류 기간은 자료마다 다르다. | 중상 | [MacTutor 전기](https://mathshistory.st-andrews.ac.uk/Biographies/De_LHopital/), [Catholic Encyclopedia](https://www.catholic.com/encyclopedia/guillaume-francois-antoine-de-lhopital), [Springer: Bradley·Petrilli·Sandifer 역주본 소개](https://link.springer.com/9783319171142) ("1691–92년 베르누이가 로피탈에게 한 강의") |
| 1693 | 로피탈, 파리 왕립 과학 아카데미 회원. | 중 | 검색 요약(MacTutor 계열). 대본에서 쓰지 않음 |
| **1694년 3월 17일** | 로피탈이 베르누이에게 편지로 제안: 해마다 일정 금액을 줄 테니 새 발견을 자신에게 알려 주고, 바리뇽 등 다른 사람에게는 보내지 말아 달라. 베르누이의 답장은 남아 있지 않으나, 이후 편지들로 보아 곧 수락한 것으로 본다. | 상 | [MacTutor: 3월 17일 편지 번역](https://mathshistory.st-andrews.ac.uk/Miscellaneous/messages/03-17), [College Board AP 2008 자료(편지 번역 포함)](https://secure-media.collegeboard.org/apc/ap08_calc_LHospital_final.rev1.pdf), [Harvard(Knill): The agreement of Bernoulli with de l'Hôpital](https://people.math.harvard.edu/~knill/teaching/math1a_2011/exhibits/bernoulli/index.html) |
| (금액) | **300**이라는 숫자는 출처가 일치한다. 단위는 갈린다. College Board 번역은 "three hundred livres(리브르)", MacTutor 영역은 "300 pounds", 영문 위키백과 한 판은 "300 Francs", 스페인어 논문은 "libras". 원문은 프랑스어 편지이므로 **리브르(livre)**가 가장 그럴듯하다고 판단한다. 대본에는 "삼백 리브르"로 쓴다. | 중상 (숫자 상, 단위 중) | 위 자료들, [Dialnet 논문](https://dialnet.unirioja.es/descarga/articulo/8832470.pdf) |
| **1694년 7월 22일** | 베르누이가 로피탈에게 보낸 편지에 0/0 꼴 극한을 분자·분모를 미분해 구하는 규칙이 처음 나온다. | 상 | [Wikipedia: L'Hôpital's rule](https://en.wikipedia.org/wiki/L%27H%C3%B4pital%27s_rule), [Springer 역주본 12장](https://rd.springer.com/chapter/10.1007/978-3-319-17115-9_12) |
| **1696** | 『무한소 해석: 곡선 이해를 위하여(Analyse des infiniment petits, pour l'intelligence des lignes courbes)』, 파리 왕립 인쇄소(Imprimerie Royale) 간행. **처음에는 저자 이름 없이(익명) 나왔다.** 미분학을 다룬 최초의 교과서로 꼽힌다. 0/0 규칙은 9장(Section IX) 첫머리 163항에 곡선 문제의 형태로 실렸다. | 상 | [MacTutor 전기](https://mathshistory.st-andrews.ac.uk/Biographies/De_LHopital/) ("the first text-book to be written on the differential calculus"), [Marsh's Library 소장 기록](https://web.marshlibrary.ie/catalogue/Record/12345), [Wikipedia: Analyse des infiniment petits](https://en.wikipedia.org/wiki/Analyse_des_infiniment_petits_pour_l%27intelligence_des_lignes_courbes), [EMS Press 논문(163항 위치)](https://ems.press/content/serial-article-files/45509) |
| 머리말 | 로피탈은 머리말에서 라이프니츠와 베르누이 형제(야코프, 요한)에게 빚졌다고 밝혔다. | 상 | [Wikipedia: Guillaume de l'Hôpital](https://en.wikipedia.org/wiki/Guillaume_de_l%27H%C3%B4pital), [MacTutor: 머리말 번역](https://mathshistory.st-andrews.ac.uk/Extras/LHopital_Preface) |
| 1704년 이후 | 로피탈이 죽은 뒤 베르누이는 책 내용 상당 부분이 자기 것이라고 주장했다. 당시에는 믿지 않는 사람이 많았다. | 중상 | [Harvard(Knill)](https://people.math.harvard.edu/~knill/teaching/math1a_2011/exhibits/bernoulli/index.html), [Wikipedia](https://en.wikipedia.org/wiki/Guillaume_de_l%27H%C3%B4pital) |
| 1922 / 1955 | 1922년 바젤에서 베르누이의 미분학 강의록(라틴어) 사본이 발견되었고, 『무한소 해석』 앞 네 장의 바탕이 된 것으로 확인됐다. 두 사람의 편지는 1955년 『요한 베르누이 서간집』으로 출간되면서 널리 알려졌다. | 중상 (1922 상, 1955 중) | [Adelphi University 초록 (Bernoulli's Lectiones de calculo differentialis)](https://scholarlyworks.adelphi.edu/esploro/outputs/bookChapter/Bernoullis-lectiones-de-calculo-differentialis/991004312582206266), 검색 요약(1955년 출간) |
| 평가 | 학계의 평가는 "베르누이가 핵심 결과와 뼈대를 주었고, 로피탈은 그것을 명료하게 정리한 저자이며 독창적인 부분도 있다" 쪽이다. "베꼈다", "훔쳤다"는 표현은 지나치다. | 상 | [Springer 역주본 소개](https://www.schweitzer-online.de/buch/Bradley/LHopitals-Analyse-des-infiniments-petits/9783319344942/B275691), Adelphi 초록 |

**대본 반영 원칙**
- 쓰는 사실: 1696 출간, 최초의 미분 교과서, 1694년 3월 제안 편지(해마다 300 리브르, 새 발견을 자신에게만), 1694년 7월 베르누이 편지에 0/0 규칙, 두 해 뒤 책에 실림, 머리말에서 도움을 밝힘.
- 편지 내용은 **직접 인용이 아니라 요지**로 쓴다("~달라고요" 간접화법).
- 쓰지 않는 것: 근시 일화, "로피탈이 정리를 돈으로 샀다/훔쳤다" 같은 단정, 1922/1955 세부.
- 정리에 로피탈 이름이 붙은 시점은 확인하지 못했다. 그래서 대본은 "실리면서 그의 이름으로 불리게 됐다"로만 쓴다.

## 3. 개념의 탄생 흐름

1. 곡선 문제에서 y = (분자)/(분모)인데 x = a에서 둘 다 0이 되는 점이 생긴다. 그 점에서 곡선의 높이를 알고 싶다(로피탈 책 163항의 문제 형태, EMS Press 논문).
2. 두 함수가 같은 점에서 0이 되면, 그 점 근처는 두 곡선 모두 접선(직선)으로 근사할 수 있다(무한소 해석의 기본 생각).
   - f(x) ≈ f′(a)(x − a), g(x) ≈ g′(a)(x − a)
3. 나누면 (x − a)가 약분된다 → f(x)/g(x) ≈ f′(a)/g′(a)
4. 즉 0/0의 값은 "두 함수가 0으로 다가가는 **빠르기(기울기)의 비**"다.
- 위 근사 논증은 f′, g′가 a에서 연속이고 g′(a) ≠ 0일 때의 직관적 설명이다. 일반적인 증명은 코시의 평균값 정리를 쓴다(19세기, 대본에서 다루지 않음). 출처: [Wikipedia: L'Hôpital's rule](https://en.wikipedia.org/wiki/L%27H%C3%B4pital%27s_rule)

## 4. 흔한 오해

1. **0/0이나 ∞/∞ 꼴이 아닌데 쓴다.** (대본에서 다룸)
   - 반례(직접 검산): lim_{x→0} (x+1)/(x+2) = 1/2. 위아래를 미분하면 1/1 = 1이 되어 틀린다.
   - 출처: [Mathwords: L'Hôpital's Rule](https://www.mathwords.com/l/l'hopitals_rule.htm) ("먼저 대입해 0/0 또는 ∞/∞인지 확인하라")
2. **몫의 미분법 (f/g)′ = (f′g − fg′)/g²으로 계산한다.** 로피탈은 분자와 분모를 **따로** 미분한다. (대본에서는 화면 설명에만 넣음)
   - 출처: [UCI Math 2A 강의 노트](https://www.math.uci.edu/~ndonalds/math2a/notes/4-4.pdf), Mathwords
3. **f′/g′의 극한이 없으면 원래 극한도 없다고 결론낸다.** 틀리다. 예: f(x) = x² sin(1/x), g(x) = x일 때 f/g → 0이지만 f′/g′ = 2x sin(1/x) − cos(1/x)는 x → 0에서 극한이 없다. (기획팀 계산, 대본에서는 쓰지 않음)
   - 출처: [Wikipedia: L'Hôpital's rule](https://en.wikipedia.org/wiki/L%27H%C3%B4pital%27s_rule) ("조건이 성립하지 않으면 결론이 틀릴 수 있다")

## 5. 예제 (검산 완료)

**채택: lim_{x→1} (x³ − 1)/(x − 1)**
- 대입: (1 − 1)/(1 − 1) = 0/0 → 조건 충족. f, g는 다항식이라 어디서나 미분 가능하고 g′(x) = 1 ≠ 0.
- 로피탈: f′(x) = 3x², g′(x) = 1 → 3·1²/1 = **3**
- 인수분해 검산: x³ − 1 = (x − 1)(x² + x + 1) → x² + x + 1 → 1 + 1 + 1 = **3** ✔
- 수치 검산: x = 1.01 → (1.030301 − 1)/0.01 = 3.0301 ✔ (분자가 분모보다 약 세 배 빠르게 0에 다가감)

**검토했으나 쓰지 않은 예제: lim_{x→0} sin x / x**
- 계산상으로는 cos x / 1 → 1로 맞다.
- 그러나 고교 교과서는 sin x의 도함수가 cos x임을 보일 때 **바로 이 극한(sin x / x → 1)을 먼저 써서** 증명한다. 그래서 로피탈로 이 극한을 "구하면" 순환 논리가 된다. 고교생 대상 영상의 예제로는 오해를 낳을 수 있어 뺐다. 필요하면 "검산용으로만 가능"이라고 소개할 수 있다.

## 6. 비유

- 두 주자가 결승선에 **동시에** 도착한다. 도착 순간 남은 거리는 둘 다 0이라 거리로는 비교할 수 없다. 대신 속도를 보면 된다. 결승 직전 남은 거리 = 속도 × 남은 시간이고 남은 시간이 같으므로, 남은 거리의 비는 속도의 비와 같다. (기획팀 자체 비유)

## 7. 실사 소재 출처 메모

| id | 출처 | 파일/검색어 | 확인 상태 |
|---|---|---|---|
| lhopital_portrait | 위키미디어 커먼즈 | `File:Guillaume de l'Hôpital.jpg` | 커먼즈 미러([osmand](https://download.osmand.net/wiki/File:Guillaume_de_l%27H%C3%B4pital.jpg))로 파일명과 라이선스(퍼블릭 도메인, 저작자 사후 70년 이하 국가 기준) 확인. 원본 페이지는 직접 열지 못함 |
| bernoulli_portrait | 위키미디어 커먼즈 (원소장: 레이크스 미술관) | `File:Portret van Johann Bernoulli (I), RP-P-1908-3095.jpg` | 미러([osmand](https://download.osmand.net/wiki/File:Portret_van_Johann_Bernoulli_(I),_RP-P-1908-3095.jpg))로 CC0 확인. 원본 페이지는 직접 열지 못함 |
| analyse_title | 위키미디어 커먼즈 | `File:L'Hospital - Analyse des infiniment petits pour l'intelligence des lignes courbes, 1715 - 1425244.jpg` | ⚠️ 위키백과 미러([wikiwand](https://wikiwand.com/EN/Analyse_des_Infiniment_Petits_pour_l'Intelligence_des_Lignes_Courbes))의 썸네일 주소에서 추정한 이름. **파일명 확인 필요.** 또한 **1715년 판**이다. 1696년 초판 속표지는 커먼즈에서 찾지 못했다 |
| (참고) | 커먼즈 PDF | `File:Analyse des infiniment petits pour l'intelligence des lignes courbes par Mr le Marquis De l'Hospita.pdf` | 미러에서 확인한 1715년 판 스캔 PDF(퍼블릭 도메인). 파일명 끝이 잘려 있어 원본 확인 필요 |

- 1696년 초판 속표지 이미지는 MAA "Mathematical Treasure" 기사(https://old.maa.org/node/871243)와 에드워드 워스 도서관(https://mathematics.edwardworthlibrary.ie/?p=68)에 있으나, 두 곳 모두 사진 자체의 재사용 조건을 확인하지 못해 **쓰지 않는다.**

## 8. 리서치 한계

- 이번 세션에서는 WebFetch가 막혀 있었다(mathshistory.st-andrews.ac.uk, commons.wikimedia.org, people.math.harvard.edu 모두 접속 불가). 위 사실은 웹 검색 결과 요약과 미러 사이트로 교차 확인한 것이다. 법무팀 검토 때 원문 페이지를 한 번 더 열어 보기를 권한다.
