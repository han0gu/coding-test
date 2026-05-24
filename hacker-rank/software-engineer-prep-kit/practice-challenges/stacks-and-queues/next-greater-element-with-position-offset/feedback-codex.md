# Codex 피드백

## 문제 조건 요약

- 각 `readings[i]`에 대해 오른쪽에서 처음 만나는 더 큰 값을 찾는다.
- 결과는 `[다음으로 큰 값, 인덱스 차이]` 형태로 반환한다.
- 더 큰 값이 없으면 `[-1, -1]`을 반환한다.
- 문제 파일은 PDF가 아니라 `next-greater-element-with-position-offset.png` 화면 이미지로 확인했다.

## 완전 탐색 풀이 리뷰

처음 작성한 완전 탐색 풀이는 문제의 핵심 정의를 잘 따랐다.

- `cur_idx` 기준으로 오른쪽 원소를 순서대로 확인했다.
- 더 큰 값을 처음 발견하면 바로 `break`해서 "오른쪽에서 처음 만나는 더 큰 값"을 정확히 찾았다.
- `readings[cur_idx:]`에서 얻은 `next_idx`가 곧 현재 위치로부터의 거리이므로 distance 계산도 맞았다.

다만 제한이 `readings.length <= 100000`이기 때문에, 완전 탐색은 최악의 경우 시간이 커진다.

```text
예: [5, 4, 3, 2, 1]
```

이런 내림차순 배열에서는 각 위치마다 끝까지 확인해야 하므로 전체 시간복잡도가 `O(n^2)`이 된다. 또 `readings[cur_idx:]`는 매 반복마다 새 리스트를 만들기 때문에 불필요한 복사 비용도 생긴다.

## 스택 풀이 리뷰

수정한 스택 풀이는 이 문제에 잘 맞는 `O(n)` 접근이다.

```python
answer = [[-1, -1] for _ in range(len(readings))]
stack = []

for cur_idx, cur_value in enumerate(readings):
    while stack and readings[stack[-1]] < cur_value:
        prev_idx = stack.pop()
        answer[prev_idx] = [cur_value, cur_idx - prev_idx]

    stack.append(cur_idx)
```

핵심은 스택에 "아직 오른쪽에서 더 큰 값을 찾지 못한 인덱스"를 넣는 것이다.

- 현재 값이 스택 맨 위 인덱스의 값보다 크면, 현재 값이 그 인덱스의 next greater element다.
- 답을 채운 인덱스는 더 이상 볼 필요가 없으므로 `pop`한다.
- 끝까지 스택에 남은 인덱스들은 오른쪽에 더 큰 값이 없으므로 기본값 `[-1, -1]`을 유지한다.

같은 값은 greater가 아니므로 `readings[stack[-1]] < cur_value` 조건을 사용한 것도 맞다. `<=`를 쓰면 같은 값을 더 큰 값으로 잘못 처리할 수 있다.

## `n = 0` 처리

처음 피드백에서는 문제 설명의 "result length n" 문장만 보고 `n = 0`이면 빈 배열을 반환해야 한다고 봤다. 하지만 실제 HackerRank 테스트가 `n = 0`에서도 `[[-1, -1]]`을 기대한다면, 현재처럼 특수 처리를 유지하는 것이 맞다.

```python
if len(readings) < 2:
    return [[-1, -1]]
```

이 코드는 `n = 1`에서도 자연스럽게 `[-1, -1]`을 반환하므로 테스트 기대값과 잘 맞는다.

## 복잡도

- 완전 탐색 풀이: 최악 `O(n^2)`
- 스택 풀이: `O(n)`
- 추가 공간: `answer`와 `stack` 때문에 `O(n)`

## 다음 문제에 적용할 점

"오른쪽에서 처음으로 조건을 만족하는 원소"를 찾는 문제는 먼저 완전 탐색으로 정의를 확인한 뒤, 제한이 크면 monotonic stack을 의심해보면 좋다. 특히 거리까지 필요할 때는 스택에 값을 직접 넣기보다 인덱스를 넣는 편이 계산하기 쉽다.
