# 기능개발 풀이 피드백

## 문제 조건 요약

- 문제 설명은 같은 디렉토리의 이미지 파일로 확인했다.
- 작업은 주어진 순서대로 배포되어야 한다.
- 뒤 작업이 먼저 완료되더라도, 앞 작업이 완료되어 배포될 때 함께 배포된다.
- 작업 개수는 최대 100개이고, 각 작업은 하루에 `speed`만큼 진행된다.

## 현재 풀이 요약

현재 풀이는 `progresses`와 `speeds`를 `deque`로 바꾼 뒤, 하루가 지날 때마다 남은 모든 작업의 진행도를 증가시킨다.

그다음 맨 앞 작업이 100 이상이면, 앞에서부터 연속으로 완료된 작업들을 `popleft()`로 제거하고 그 개수를 `answer`에 추가한다.

```python
from collections import deque

def solution(progresses, speeds):
    answer = []

    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        if progresses[0] >= 100:
            pop_cnt = 0

            while progresses and progresses[0] >= 100:
                pop_cnt += 1

                progresses.popleft()
                speeds.popleft()

            answer.append(pop_cnt)

    return answer
```

## 잘한 점

- 앞 작업부터 배포되어야 한다는 조건을 `deque`의 맨 앞 원소로 잘 표현했다.
- 완료된 작업을 `popleft()`로 제거하는 흐름은 큐 문제의 성격과 잘 맞는다.
- 뒤 작업이 먼저 100 이상이 되더라도, 앞 작업이 완료되기 전에는 배포하지 않는 조건을 자연스럽게 지킨다.
- 예제와 추가 테스트에서 기대한 결과와 일치했다.

## 개선하면 좋은 점

현재 풀이의 핵심 아쉬움은 하루씩 직접 시뮬레이션한다는 점이다.

```python
for i in range(len(progresses)):
    progresses[i] += speeds[i]
```

작업 개수가 최대 100개라서 이 방식도 문제 제한 안에서는 통과 가능성이 높다. 하지만 문제를 더 단순하게 보면, 실제로 매일 진행도를 올릴 필요는 없다.

각 작업이 며칠 뒤 완료되는지만 먼저 계산하면 된다.

```python
days = (100 - progress + speed - 1) // speed
```

여기서 `(100 - progress + speed - 1) // speed`는 `ceil((100 - progress) / speed)`를 정수 연산으로 계산하는 표현이다.

예를 들어 남은 작업량이 `5`, 하루 속도가 `4`라면 실제로는 `2`일이 필요하다. 정수 나눗셈 `5 // 4`는 `1`이 되므로 부족하고, `5 + 4 - 1`을 한 뒤 `4`로 나누면 `2`가 된다.

수학적으로는 양의 정수 `a`, `b`에 대해 아래 공식이 성립한다.

```python
ceil(a / b) == (a + b - 1) // b
```

이 문제에서는 `a = 100 - progress`, `b = speed`이다.

## 개선 예시

완료 예정일을 먼저 계산한 뒤, 앞 작업의 배포일보다 작거나 같은 작업들을 같은 배포 묶음으로 세면 된다.

```python
def solution(progresses, speeds):
    answer = []
    days = []

    for progress, speed in zip(progresses, speeds):
        days.append((100 - progress + speed - 1) // speed)

    current = days[0]
    count = 0

    for day in days:
        if day <= current:
            count += 1
        else:
            answer.append(count)
            current = day
            count = 1

    answer.append(count)
    return answer
```

이 방식은 큐를 직접 쓰지는 않지만, 앞에서부터 작업을 확인하면서 배포 묶음을 만든다는 점에서 문제 조건을 더 직접적으로 표현한다.

## 추가 테스트

현재 풀이로 직접 실행한 테스트는 모두 기대값과 일치했다.

```text
progresses=[93, 30, 55], speeds=[1, 30, 5] -> [2, 1]
progresses=[95, 90, 99, 99, 80, 99], speeds=[1, 1, 1, 1, 1, 1] -> [1, 3, 2]
progresses=[99], speeds=[1] -> [1]
progresses=[99, 99, 99], speeds=[1, 1, 1] -> [3]
progresses=[90, 90, 90], speeds=[10, 5, 1] -> [1, 1, 1]
progresses=[10, 99, 99], speeds=[10, 1, 1] -> [3]
progresses=[20, 99, 80], speeds=[10, 1, 5] -> [3]
progresses=[90, 80, 70], speeds=[10, 10, 10] -> [1, 1, 1]
```

## 다음 문제에 적용할 점

시뮬레이션 문제처럼 보여도, 매 단계를 실제로 진행해야 하는지 먼저 확인하는 것이 좋다. 이 문제는 하루씩 진행도를 갱신하지 않고도 각 작업의 완료 예정일을 계산해서 해결할 수 있다.
