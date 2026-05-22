# 15970 화살표 그리기 풀이 피드백

## 문제 조건 요약

각 점은 `(위치, 색깔)`로 주어집니다. 각 점에서 같은 색깔을 가진 다른 점 중 가장 가까운 점으로 화살표를 그렸을 때, 모든 화살표 길이의 합을 구하는 문제입니다.

문제 조건상 각 색깔은 2개 이상의 점을 가지므로, 모든 점은 항상 같은 색깔의 다른 점을 하나 이상 찾을 수 있습니다.

## 현재 풀이 평가

현재 `main.py`는 각 점 `p1`에 대해 모든 점 `p2`를 다시 확인하면서, 색깔이 같은 점 중 가장 가까운 거리만 남기는 방식입니다.

```python
for p1 in candidates:
    p1_len = max_len

    for p2 in candidates:
        if p1 == p2:
            continue

        if p1[1] == p2[1]:
            p1_len = min(p1_len, abs(p1[0] - p2[0]))

    answer += p1_len
```

이 접근은 문제의 요구사항을 그대로 코드로 옮긴 풀이입니다.

- 기준 점을 하나 고릅니다.
- 같은 색깔의 다른 점들을 모두 봅니다.
- 그중 가장 짧은 거리만 더합니다.

완전탐색 문제에서는 이렇게 조건을 직접적으로 구현하는 방식이 실수를 줄이는 좋은 선택입니다.

## 잘한 점

문제를 어렵게 바꾸지 않고, "같은 색깔 중 가장 가까운 점"이라는 핵심 조건을 그대로 구현했습니다.

특히 `min`과 `abs`를 사용해서 거리의 최솟값을 갱신한 부분은 명확합니다.

```python
p1_len = min(p1_len, abs(p1[0] - p2[0]))
```

이 코드는 `p1`과 `p2`의 위치 차이를 구한 뒤, 지금까지 찾은 가장 짧은 거리와 비교합니다.

## 개선점 1: 초기값의 의미를 더 분명하게 하기

현재 코드는 `p1_len`의 초기값으로 `max_len`을 사용합니다.

```python
max_len = max(c[0] for c in candidates)

for p1 in candidates:
    p1_len = max_len
```

이 코드도 제출 조건 안에서는 동작합니다. 모든 점마다 같은 색의 다른 점이 존재하기 때문에 `p1_len`은 반복문 안에서 실제 거리로 갱신됩니다.

다만 `max_len`은 "가장 큰 위치"라는 뜻이라서, "아직 최소 거리를 찾지 못했다"는 의미를 표현하기에는 조금 애매합니다. 이런 경우에는 `float("inf")`를 쓰면 의도가 더 분명해집니다.

```python
for p1 in candidates:
    p1_len = float("inf")
```

`float("inf")`는 무한대를 뜻하므로, 어떤 실제 거리와 비교해도 처음 한 번은 반드시 실제 거리로 갱신됩니다.

## 개선점 2: 정렬을 이용하면 더 효율적으로 풀 수 있음

현재 풀이는 모든 점 쌍을 비교합니다. 점의 개수가 `N`개라면 대략 `N * N`번 비교하므로 시간 복잡도는 `O(N^2)`입니다.

이 문제는 색깔별로 위치를 모은 뒤 정렬하면 더 단순하게 볼 수 있습니다.

같은 색깔의 점들이 아래처럼 있다고 해봅시다.

```text
0  3  5  10
```

위치 `5`에서 가장 가까운 같은 색 점은 멀리 있는 `0`이나 `10`까지 볼 필요 없이, 정렬했을 때 바로 왼쪽 `3` 또는 바로 오른쪽 `10` 중 하나입니다.

즉, 정렬된 상태에서는 각 점마다 인접한 점만 확인하면 됩니다.

## 개선 예시

아래 코드는 현재 풀이의 아이디어를 유지하되, 색깔별로 위치를 모아서 정렬하는 방식입니다.

```python
n = int(input())

points_by_color = {}

for _ in range(n):
    x, color = map(int, input().split())

    if color not in points_by_color:
        points_by_color[color] = []

    points_by_color[color].append(x)

answer = 0

for positions in points_by_color.values():
    positions.sort()

    for i in range(len(positions)):
        distance = float("inf")

        if i > 0:
            distance = min(distance, positions[i] - positions[i - 1])

        if i < len(positions) - 1:
            distance = min(distance, positions[i + 1] - positions[i])

        answer += distance

print(answer)
```

이 방식은 같은 색깔끼리만 따로 보고, 정렬된 위치에서 왼쪽과 오른쪽 이웃만 비교합니다.

## 시간 복잡도 비교

현재 풀이:

```text
O(N^2)
```

모든 점에 대해 모든 점을 다시 확인합니다.

정렬을 이용한 풀이:

```text
O(N log N)
```

색깔별로 위치를 정렬한 뒤, 각 위치는 한 번씩만 확인합니다.

## 다음 문제에 적용할 점

"가장 가까운 값"을 찾는 문제에서는 먼저 정렬을 떠올려보면 좋습니다.

정렬했을 때 가장 가까운 값은 보통 멀리 떨어진 값이 아니라 바로 옆에 있는 값입니다. 따라서 모든 쌍을 비교하기 전에, 정렬 후 인접한 값만 봐도 되는 문제인지 확인해보세요.
