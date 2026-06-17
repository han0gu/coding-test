# 네트워크 풀이 피드백

## 문제 조건 요약

- 문제 설명은 같은 디렉토리의 이미지 파일로 확인했다.
- 컴퓨터 `i`와 `j`가 연결되어 있으면 `computers[i][j] == 1`이다.
- 직접 연결뿐 아니라 간접적으로 연결된 컴퓨터들도 같은 네트워크에 속한다.
- 목표는 전체 네트워크, 즉 연결 컴포넌트의 개수를 세는 것이다.
- 컴퓨터 개수 `n`은 1 이상 200 이하이다.

## 처음 풀이 요약

처음 풀이는 `computers` 행렬의 각 칸 `(r, c)`를 순회하면서, 연결 정보가 `1`이고 아직 방문하지 않은 칸이면 BFS를 시작했다.

```python
visited = [[False] * col_cnt for _ in range(row_cnt)]
```

큐에는 `(r, c)` 형태의 좌표를 넣는다.

```python
q.append((r, c))
```

큐에서 꺼낸 뒤에는 대칭 위치까지 방문 처리한다.

```python
visited[cur_r][cur_c] = True
visited[cur_c][cur_r] = True
```

그리고 현재 행에서 연결된 칸들을 다시 큐에 넣는다.

```python
for i in range(col_cnt):
    if not visited[cur_r][i] and computers[cur_r][i] == 1:
        q.append((cur_r, i))
        q.append((i, cur_r))
```

## 처음 풀이에서 잘한 점

- BFS로 연결된 대상을 따라가려는 방향은 문제 분류와 잘 맞는다.
- 예제와 기본적인 추가 케이스에서는 올바른 결과가 나온다.
- `computers[i][j]`와 `computers[j][i]`가 대칭이라는 점을 고려해 양쪽을 방문 처리하려 한 점도 좋은 관찰이다.

직접 확인한 테스트:

```text
n=3, [[1,1,0],[1,1,0],[0,0,1]] -> 2
n=3, [[1,1,0],[1,1,1],[0,1,1]] -> 1
n=1, [[1]] -> 1
모두 고립된 3개 컴퓨터 -> 3
두 쌍으로 분리된 4개 컴퓨터 -> 2
체인으로 모두 연결된 4개 컴퓨터 -> 1
```

## 처음 풀이의 핵심 문제

처음 풀이의 가장 큰 문제는 **방문 대상을 행렬 칸으로 잡은 것**이었다.

이 문제의 그래프 노드는 `(r, c)` 칸이 아니라 컴퓨터 번호다.

```text
노드: 0번 컴퓨터, 1번 컴퓨터, 2번 컴퓨터, ...
간선: computers[i][j] == 1
```

따라서 방문 배열도 2차원이 아니라 1차원이면 충분하다.

```python
visited = [False] * n
```

처음처럼 행렬 칸을 방문 대상으로 보면, 연결이 많은 그래프에서 같은 컴퓨터나 같은 연결 정보를 큐에 중복으로 많이 넣게 된다. 특히 완전 연결 그래프에서는 성능 차이가 크게 난다.

직접 확인한 성능:

```text
완전 연결 그래프 n=20  -> 약 0.0057초
완전 연결 그래프 n=50  -> 약 0.2068초
완전 연결 그래프 n=100 -> 약 2.4224초
완전 연결 그래프 n=200 -> 30초 안에 끝나지 않아 중단
```

제한이 `n <= 200`이므로 처음 구조는 시간 초과 위험이 크다.

## 현재 풀이 요약

현재 `main.py`는 위 피드백을 반영해 컴퓨터 번호를 노드로 보고 BFS를 수행한다.

```python
visited = [False] * n
```

아직 방문하지 않은 컴퓨터를 만나면 새 네트워크의 시작점으로 보고, 큐에 넣는 순간 방문 처리한다.

```python
if not visited[i]:
    q.append(i)
    visited[i] = True
    answer += 1
```

BFS 안에서도 연결된 컴퓨터를 발견하면 바로 방문 처리한 뒤 큐에 추가한다.

```python
if not visited[j] and computers[cur_node][j] == 1:
    q.append(j)
    visited[j] = True
```

이 구조에서는 각 컴퓨터를 최대 한 번 방문하고, 각 컴퓨터마다 한 행의 연결 정보를 확인한다. 인접 행렬을 쓰는 문제이므로 시간복잡도는 `O(n^2)`이다.

## 개선 방향

컴퓨터 번호를 노드로 보고 BFS를 돌리면 된다.

흐름은 다음과 같다.

```text
1. 0번부터 n-1번 컴퓨터를 순회한다.
2. 아직 방문하지 않은 컴퓨터를 만나면 새 네트워크를 찾은 것이므로 answer += 1.
3. 그 컴퓨터를 시작점으로 BFS를 돌린다.
4. 연결된 모든 컴퓨터를 방문 처리한다.
5. 다음 미방문 컴퓨터를 만나면 새 네트워크로 센다.
```

핵심은 BFS를 시작할 때 네트워크 개수를 하나 증가시키고, BFS 내부에서는 같은 네트워크에 속한 컴퓨터들을 모두 방문 처리하는 것이다.

## BFS의 `visited` 처리 타이밍

BFS에서는 보통 노드를 큐에 넣는 순간 방문 처리하는 편이 좋다.

```python
q.append(start)
visited[start] = True
```

인접 노드를 발견했을 때도 마찬가지다.

```python
if computers[cur][nxt] == 1 and not visited[nxt]:
    visited[nxt] = True
    q.append(nxt)
```

방문 처리를 큐에서 꺼낼 때 하면, 같은 노드가 큐에 여러 번 들어갈 수 있다. 예를 들어 여러 노드가 같은 `nxt`로 연결되어 있으면, `nxt`가 아직 pop되지 않은 동안 다른 경로에서 다시 큐에 들어갈 수 있다.

반대로 큐에 넣는 순간 방문 처리하면, 그 노드는 이미 탐색 예정인 상태가 되므로 중복 삽입을 막을 수 있다.

이번 문제의 최신 풀이에서는 이 점을 잘 반영했다.

```python
if not visited[i]:
    q.append(i)
    visited[i] = True
    answer += 1
```

그리고 인접 노드를 추가할 때도 바로 방문 처리한다.

```python
if not visited[j] and computers[cur_node][j] == 1:
    q.append(j)
    visited[j] = True
```

이 방식은 정답성뿐 아니라 성능 면에서도 더 안정적이다.

## 개선 예시

```python
from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n

    for start in range(n):
        if visited[start]:
            continue

        answer += 1
        q = deque([start])
        visited[start] = True

        while q:
            cur = q.popleft()

            for nxt in range(n):
                if computers[cur][nxt] == 1 and not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)

    return answer
```

이 방식은 각 컴퓨터를 한 번씩 방문하고, 각 컴퓨터에서 연결 정보를 한 행씩 확인한다. 인접 행렬을 쓰는 문제이므로 시간복잡도는 `O(n^2)` 정도로 보면 된다.

## 다음 문제에 적용할 점

그래프 문제에서 가장 먼저 정해야 할 것은 **노드가 무엇인가**이다.

이번 문제에서는 `computers[r][c]` 칸이 아니라 `r번 컴퓨터` 자체가 노드다. 방문 배열을 노드 기준으로 잡으면 BFS/DFS 구조가 훨씬 단순해지고, 중복 탐색도 줄어든다.
