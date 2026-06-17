"""
BFS

네트워크 시작점을 q에 추가, answer += 1,
-> 특정 노드를 pop 하면서 인접 노드를 추가
-> q가 비어 있으면 해당 네트워크 처리 완료
"""
from collections import deque

def solution(n, computers):
    answer = 0

    visited = [False] * n
    q = deque()

    for i in range(n):
        if visited[i]:
            continue

        # 시작점 처리
        q.append(i)
        visited[i] = True
        answer += 1

        # 인접 노드 처리
        while q:
            cur_node = q.popleft()

            for j in range(n):
                if not visited[j] and computers[cur_node][j] == 1:
                    q.append(j)
                    visited[j] = True

    return answer
