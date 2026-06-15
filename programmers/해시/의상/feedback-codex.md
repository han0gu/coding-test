# 의상 풀이 피드백

## 문제 조건 요약

- 문제 설명은 같은 디렉토리의 이미지 파일로 확인했다.
- 코니는 각 의상 종류별로 최대 1개의 의상만 입을 수 있다.
- 하루에 최소 1개 이상의 의상은 입어야 한다.
- `clothes`의 길이는 1 이상 30 이하이고, 같은 이름의 의상은 없다.

## 풀이가 바뀐 흐름

`53d153c` 커밋에서는 `defaultdict(list)`로 종류별 의상을 묶고, 카테고리 조합을 모두 만든 뒤 각 조합의 경우의 수를 더했다.

```python
from collections import defaultdict
from itertools import combinations

def solution(clothes):
    answer = 0

    category_dict = defaultdict(list)
    for clth, cate in clothes:
        category_dict[cate].append(clth)

    keys = category_dict.keys()
    all_combs = []
    for i in range(len(keys)):
        all_combs.extend(combinations(keys, i+1))

    for comb in all_combs:
        cnt = 1
        for c in comb:
            cnt *= len(category_dict[c])
        answer += cnt

    return answer
```

이 풀이는 조합을 세는 방향 자체는 맞다. 예를 들어 `headgear`와 `eyewear`를 둘 다 선택하는 경우에는 `headgear` 의상 수와 `eyewear` 의상 수를 곱해야 한다.

문제는 카테고리 조합을 전부 실제로 만든다는 점이다. 의상 수가 최대 30개이고, 최악의 경우 모든 의상이 서로 다른 종류라면 카테고리도 30개가 된다. 이때 가능한 카테고리 조합 수는 `2^30 - 1`개라서 시간 초과가 난다.

## `Counter`로 바꾼 뒤에도 남은 병목

이후 `72a2cc0` 커밋에서는 종류별 실제 의상 목록을 저장하지 않고, `Counter`로 종류별 개수만 세도록 바뀌었다.

```python
from collections import Counter
from itertools import combinations
import math

def solution(clothes):
    answer = 0

    category_dict = Counter([c[1] for c in clothes])

    keys = category_dict.keys()
    for i in range(len(keys)):
        for comb in combinations(keys, i+1):
            cnt = math.prod([category_dict[x] for x in comb])
            answer += cnt

    return answer
```

이 변화는 좋다. 이 문제에서는 구체적인 의상 이름보다 종류별 개수만 필요하기 때문이다. 그래서 `defaultdict(list)`보다 `Counter`가 더 직접적인 자료구조다.

하지만 시간 초과 원인은 여전히 남아 있었다. `combinations(keys, i+1)`로 모든 카테고리 조합을 순회하고 있기 때문이다. 자료구조는 가벼워졌지만, 탐색해야 하는 조합 수는 그대로 `2^k - 1`개다.

## 2진수로 부분집합을 순회한 풀이

이후 커밋으로는 남아 있지 않지만, 중간에 2진수를 이용해 카테고리 선택 여부를 표현한 풀이도 있었다.

```python
from collections import Counter

def solution(clothes):
    answer = 0

    category_dict = Counter([c[1] for c in clothes])

    keys = list(category_dict.keys())
    len_cate = len(keys)

    for i in range(1, 2**len_cate):
        binary = bin(i)[2:].zfill(len_cate)

        cnt = 1
        for i, v in enumerate(binary):
            if v != '0':
                cnt = cnt * int(v) * category_dict[keys[i]]

        answer += cnt

    return answer
```

이 풀이도 아이디어 자체는 자연스럽다. 각 카테고리를 `선택한다 / 선택하지 않는다`로 나누고, `1`인 자리의 카테고리만 곱해서 경우의 수를 더하는 방식이다.

하지만 성능 병목은 그대로 남아 있다. `for i in range(1, 2**len_cate)`가 모든 카테고리 부분집합을 순회하기 때문이다. 즉 `combinations`를 직접 쓰지 않았을 뿐, 실제로는 같은 수의 조합을 모두 확인하고 있다.

또 `binary = bin(i)[2:].zfill(len_cate)`처럼 매번 문자열을 만들고 순회하므로, 같은 `2^k` 방식 안에서도 추가 비용이 더 붙는다. 따라서 이 문제에서는 2진수 표현으로 바꿔도 시간 초과를 해결할 수 없다.

## 최종 개선 아이디어

이 문제는 카테고리 조합을 직접 만들 필요가 없다.

각 카테고리마다 선택지는 다음과 같다.

```text
그 종류의 의상 중 하나를 입는 경우: count개
그 종류를 아예 안 입는 경우: 1개
```

따라서 카테고리별로 `(count + 1)`을 모두 곱하면 된다. 이 값에는 모든 종류를 안 입는 경우도 1개 포함되어 있으므로, 마지막에 `1`을 빼면 정답이 된다.

현재 `main.py`는 이 방식으로 정리되어 있다.

```python
from collections import Counter

def solution(clothes):
    answer = 1

    category_dict = Counter(cate for _, cate in clothes)

    for v in category_dict.values():
        answer *= v + 1

    return answer - 1
```

## 현재 풀이에서 좋은 점

- 종류별 개수만 필요하다는 점을 보고 `Counter`를 사용했다.
- 카테고리 조합을 직접 만들지 않아 시간 초과 병목을 제거했다.
- `안 입는 경우`를 `+1`로 포함하고, 마지막에 아무것도 안 입는 경우만 빼는 방식이 문제 조건과 잘 맞는다.
- `Counter(cate for _, cate in clothes)`처럼 필요한 값만 바로 꺼내서 세는 표현도 깔끔하다.

## 복잡도

`n`을 전체 의상 수, `k`를 의상 종류 수라고 하면 현재 풀이는 다음 정도로 볼 수 있다.

- 종류별 개수 세기: `O(n)`
- 종류별 경우의 수 곱하기: `O(k)`
- 전체 시간복잡도: `O(n + k)`

반면 이전 조합 기반 풀이와 2진수 부분집합 풀이 모두 카테고리 조합을 전부 보므로 최악의 경우 `O(2^k)`에 가까웠다. 이번 문제의 시간 초과는 이 차이 때문에 발생했다.

## 추가 테스트

현재 풀이로 직접 실행한 테스트는 모두 기대값과 일치했다.

```text
[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]] -> 5
[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]] -> 3
[["a", "x"]] -> 1
[["a", "x"], ["b", "y"], ["c", "z"]] -> 7
[["a", "x"], ["b", "x"], ["c", "y"], ["d", "y"]] -> 8
```

## 다음 문제에 적용할 점

조합 문제처럼 보여도 실제 조합을 전부 만들어야 하는 것은 아니다. `combinations`든 2진수 부분집합 순회든 모든 선택 조합을 직접 나열하면 결국 `2^k` 비용이 든다. 각 그룹에서 선택지가 독립적으로 곱해지는 구조라면, `직접 나열`보다 `선택지 수의 곱`으로 계산할 수 있는지 먼저 확인하는 것이 좋다.
