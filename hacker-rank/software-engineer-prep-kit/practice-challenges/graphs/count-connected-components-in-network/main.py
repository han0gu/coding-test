#!/bin/python3

#
# Complete the 'countIsolatedCommunicationGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY links
#  2. INTEGER n
#

"""
0 1
1 0
"""

"""
0 1 0 0
1 0 0 0
0 0 0 1
0 0 1 0
"""

"""
0 1 1
1 0 1
1 1 0
"""

"""
1
2
0 1
3

0 1 0
1 0 0
0 0 0
"""

def paint_with_one(board, start, end):
    board[start][end] = 1
    board[end][start] = 1

def countIsolatedCommunicationGroups(links, n):

    if n == 1:
        return 1

    answer = 0

    board = [[0] * n for _ in range(n)]
    # print('init board', board)

    for start, end in links:
        paint_with_one(board, start, end)
    # print('paint board', board)

    visited = [False] * n
    stack = []
    for node in range(n):
        if visited[node]:
            continue

        answer += 1
        visited[node] = True
        stack.append(node)

        while stack:
            cur = stack.pop()

            for near in range(n):
                if not visited[near] and board[cur][near] == 1:
                    visited[near] = True
                    stack.append(near)

    return answer

if __name__ == '__main__':
    links_rows = int(input().strip())
    links_columns = int(input().strip())

    links = []

    for _ in range(links_rows):
        links.append(list(map(int, input().rstrip().split())))

    n = int(input().strip())

    result = countIsolatedCommunicationGroups(links, n)

    print(result)
