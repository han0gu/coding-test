from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    visited = [[False] * m for _ in range(n)]

    visited[0][0] = True
    q = deque([(0, 0, 1)])

    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

    while q:
        r, c, acc = q.popleft()

        if r == n - 1 and c == m - 1:
            return acc

        for d_r, d_c in directions:
            new_r = r + d_r
            new_c = c + d_c

            if (
                0 <= new_r < n and
                0 <= new_c < m and
                not visited[new_r][new_c]
                and maps[new_r][new_c] == 1
            ):
                visited[new_r][new_c] = True
                q.append((new_r, new_c, acc + 1))

    return -1
