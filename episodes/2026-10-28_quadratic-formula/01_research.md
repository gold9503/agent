# 리서치 노트: 근의 공식

- **난이도 모드:** `middle`
- **교육과정 위치:** 중학교 3학년 수학, 이차방정식. 풀이 방법(인수분해, 완전제곱식, 근의 공식)을 배우며, 중3 범위에서는 실근만 다룬다.
  - ⚠️ 성취기준 코드와 원문은 국가교육과정정보센터(ncic.go.kr)에서 확인해야 한다. 이번 리서치에서는 원문을 찾지 못했다.

## 1. 정의
이차방정식 `ax² + bx + c = 0 (a ≠ 0)`의 해는 다음과 같다.

`x = (−b ± √(b² − 4ac)) / 2a`

## 2. 역사

| 시기 | 내용 | 신뢰도 | 출처 |
|---|---|---|---|
| 기원전 18세기 초 (함무라비 시대) | 바빌로니아 점토판(BM 13901)에 이차방정식 문제와 완전제곱식에 해당하는 계산 절차가 나온다. 일반 공식이 아니라 문제별 계산 순서다. | 중상 | [Stony Brook: Early History of Quadratic Equations](https://www.math.stonybrook.edu/~moira/courses/SBU102-sp2025/example.html), [Babylonian mathematics](https://ipfs.ssi.eecc.de/ipns/en.wikipedia-on-ipfs.org/wiki/Babylonian_mathematics) |
| 서기 628년 | 인도의 브라마굽타가 『브라마스푸타싯단타』에서 근의 공식에 해당하는 규칙을 기호 없이 운문(말)으로 서술했다. | 중 | [Brāhmasphuṭasiddhānta (Wikipedia)](https://en.wikipedia.org/wiki/Br%C4%81hmasphu%E1%B9%ADasiddh%C4%81nta) |
| 820년경 | 바그다드 '지혜의 집'의 학자 알 콰리즈미가 『알 자브르와 알 무카발라』에서 이차방정식을 유형별로 정리하고 정사각형 완성(기하학적 증명)으로 풀었다. 대표 예제는 x² + 10x = 39이고 답은 3이다. 음수 해(−13)는 인정하지 않았다. | 상 | [Harvard: Completion of Squares](https://people.math.harvard.edu/archive/21a_fall_05/exhibits/completion/index.html), [Redlands: Al-Khwarizmi's Completing the Square](https://bulldog2.redlands.edu/fac/Beery/math115/m115_activ_complsq.htm), [MAA](https://old.maa.org/node/116293) |
| 같은 책 | 책은 유산 분배, 토지 측량, 거래 같은 실용 문제를 다룬다. 기호가 없어 문제와 풀이를 모두 문장으로 썼다. | 상 | [Al-Khwarizmi Contributions (PDF)](https://martin.kcvs.ca/math/math499/projects/alkhwarizmi/contributions%20of%20al-khwarizmi.pdf) |
| 어원 | 책 제목의 'al-jabr'에서 algebra(대수학)가, 그의 이름(라틴어 표기 Algoritmi)에서 algorithm(알고리즘)이 나왔다. | 상 | 위 MAA, KCVS 자료 |
| 16~17세기 이후 | 문자 계수를 쓰는 오늘날의 표기는 비에트, 데카르트 이후 기호 대수가 발전하면서 자리 잡았다. 정확한 '최초' 표기자는 자료마다 달라 **대본에서 단정하지 않는다.** | 중하 | 여러 2차 자료 |

## 3. 개념의 탄생 흐름
문제별 계산 순서(바빌로니아) → 말로 쓴 일반 규칙(브라마굽타) → 유형 분류와 그림을 이용한 증명(알 콰리즈미) → 기호로 압축한 공식(근대)

## 4. 흔한 오해
1. "근의 공식은 인수분해가 안 될 때만 쓰는 특수한 공식이다." → 실제로는 모든 이차방정식에 통하는 일반 해법이다. 인수분해가 지름길이다.
2. "근의 공식은 외워야만 하는 것이다." → 완전제곱식을 일반화하면 직접 유도할 수 있다.
3. "판별식이 음수면 답이 틀린 것이다." → 실수 범위에 해가 없을 뿐이다. 고등학교에서 복소수로 확장된다.

## 5. 공식 풀이 예제 (검산 완료)
`x² + 10x − 39 = 0` → a = 1, b = 10, c = −39
- b² − 4ac = 100 + 156 = 256, √256 = 16
- x = (−10 + 16) / 2 = 3, x = (−10 − 16) / 2 = −13
- 정사각형 그림 풀이: 10x를 네 조각(각각 2.5 × x)으로 나눠 붙이고 귀퉁이 4 × 2.5² = 25를 채운다 → (x + 5)² = 64 → x = 3
- 일반식: (x + b/2a)² = (b² − 4ac) / 4a²이므로 b² − 4ac의 부호가 완성된 정사각형 넓이의 부호를 결정한다.
