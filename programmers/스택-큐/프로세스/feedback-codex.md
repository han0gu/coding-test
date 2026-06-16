# 프로세스 풀이 피드백

## 문제 조건 요약

- 문제 설명은 같은 디렉토리의 이미지 파일로 확인했다.
- 대기 큐의 맨 앞 프로세스를 꺼냈을 때, 큐 안에 더 높은 우선순위가 있으면 다시 뒤에 넣는다.
- 더 높은 우선순위가 없다면 해당 프로세스를 실행한다.
- `location`에 있던 프로세스가 몇 번째로 실행되는지 반환해야 한다.
- `priorities`의 길이는 1 이상 100 이하이고, 우선순위는 숫자가 클수록 높다.

## `1d845de` 커밋의 풀이

`1d845de7ecf6512680d9913d42796ae97fe7047e` 커밋의 풀이는 먼저 우선순위를 내림차순으로 정렬해서, 앞으로 실행되어야 할 우선순위 순서를 만들었다.

```python
priorities_q = deque(sorted(priorities, reverse=True))
```

그리고 원래 `priorities` 배열을 반복해서 순회하면서, 아직 처리되지 않았고 현재 실행되어야 할 우선순위와 같은 프로세스를 실행 처리했다.

```python
priorities_processed = [-1] * len(priorities)

order = 1
while priorities_q:
    for i, v in enumerate(priorities):
        if priorities_processed[i] == -1 and v == priorities_q[0]:
            priorities_processed[i] = order
            order += 1
            priorities_q.popleft()

return priorities_processed[location]
```

이 접근은 정답 가능성이 높은 풀이였다. 특히 `sorted(priorities, reverse=True)`를 이용해서 현재 실행되어야 할 우선순위를 미리 관리한 점이 좋았다. 이 덕분에 매번 남은 큐 전체에서 최댓값을 다시 찾지 않아도 된다.

또 같은 우선순위가 여러 개 있을 때 원래 배열을 앞에서부터 순회하므로, 같은 우선순위끼리는 기존 대기 순서가 유지된다.

다만 문제에서 설명한 큐 동작을 그대로 표현한 코드는 아니었다. 실제 규칙은 `popleft()`로 꺼내고, 실행할 수 없으면 `append()`로 다시 뒤에 넣는 흐름인데, 이 풀이에서는 원본 배열을 반복 순회하면서 실행 순서를 재구성했다.

또 `priorities_processed`에 모든 프로세스의 실행 순서를 끝까지 기록한 뒤 `location`을 조회했다. 실제로는 `location` 프로세스가 실행되는 순간 바로 반환할 수 있다.

## 중간 피드백: `any()` 큐 풀이

중간 피드백에서 문제 규칙을 더 직접적으로 보여주기 위해 아래처럼 `any()`를 활용한 큐 풀이를 제안했었다.

```python
from collections import deque

def solution(priorities, location):
    q = deque((i, p) for i, p in enumerate(priorities))
    order = 0

    while q:
        idx, priority = q.popleft()

        if any(priority < other_priority for _, other_priority in q):
            q.append((idx, priority))
        else:
            order += 1
            if idx == location:
                return order
```

이 코드는 문제 설명의 규칙을 그대로 옮긴 형태라서 이해하기는 쉽다.

하지만 좋은 개선안이라고 보기는 어렵다. `any(...)`가 매번 큐 안의 나머지 프로세스를 훑기 때문에 최악의 경우 `O(n^2)`에 가깝다.

이 문제는 `n <= 100`이라 통과 자체는 가능하지만, 성능과 접근 방향만 보면 기존 풀이의 핵심 아이디어였던 "정렬된 우선순위 목록을 따로 두고 현재 실행 가능 여부를 판단하는 방식"이 더 좋았다.

따라서 `any()` 풀이는 설명용으로는 괜찮지만, 이 문제의 개선 방향으로는 기존 풀이의 장점을 유지하는 쪽이 더 낫다.

## 최종 개선 방향

최종적으로는 기존 풀이의 좋은 점과 큐 시뮬레이션의 직관성을 합치는 방향으로 개선했다.

- 기존 풀이의 장점: 정렬된 우선순위 목록으로 현재 실행되어야 할 우선순위를 빠르게 확인한다.
- 큐 풀이의 장점: 실제 프로세스 큐를 `popleft()`와 `append()`로 회전시킨다.
- 추가 개선: `location` 프로세스가 실행되는 순간 바로 반환한다.

현재 `main.py`는 이 흐름을 반영한 상태다.

```python
from collections import deque

def solution(priorities, location):
    sorted_priorities = deque(sorted(priorities, reverse=True))
    process_q = deque((i, p) for i, p in enumerate(priorities))

    order = 0
    while process_q:
        i, p = process_q.popleft()

        if p == sorted_priorities[0]:
            order += 1
            sorted_priorities.popleft()

            if i == location:
                return order
        else:
            process_q.append((i, p))
```

이 방식은 `1d845de` 풀이의 핵심 아이디어를 버린 것이 아니라, 더 큐답게 정리한 것이다.

## 현재 풀이에서 좋은 점

- `sorted_priorities`로 현재 실행되어야 할 우선순위를 바로 확인한다.
- `process_q`에 `(원래 인덱스, 우선순위)`를 저장해서 `location` 프로세스를 추적한다.
- 실행할 수 없는 프로세스는 `append()`로 다시 뒤에 넣어 문제의 큐 동작을 직접 표현한다.
- 실행 가능한 프로세스가 `location`이면 즉시 반환하므로 불필요한 실행 순서 기록이 없다.
- 같은 우선순위끼리는 큐 순서대로 처리되므로 기존 대기 순서가 유지된다.

## 추가 테스트

현재 풀이로 직접 실행한 테스트는 모두 기대값과 일치했다.

```text
priorities=[2, 1, 3, 2], location=2 -> 1
priorities=[1, 1, 9, 1, 1, 1], location=0 -> 5
priorities=[1], location=0 -> 1
priorities=[3, 3, 3], location=1 -> 2
priorities=[1, 3, 2, 1], location=0 -> 4
priorities=[1, 3, 2, 1], location=3 -> 3
priorities=[2, 1, 2], location=1 -> 3
```

작은 랜덤 케이스도 표준 큐 시뮬레이션 결과와 비교했고, 차이가 없었다.

## 다음 문제에 적용할 점

스택/큐 문제에서는 자료구조의 동작을 코드에 직접 드러내는 것이 이해와 디버깅에 유리하다.

다만 큐 전체를 매번 훑는 방식이 보이면 무조건 그대로 쓰기보다, 이번 문제처럼 정렬된 보조 자료구조를 두고 반복 조회 비용을 줄일 수 있는지 같이 생각해보면 좋다.

이번 풀이의 핵심 교훈은 다음과 같다.

```text
문제 규칙을 코드에 드러내되,
기존 풀이의 좋은 아이디어까지 버릴 필요는 없다.
```
