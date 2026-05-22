"""
음이 아닌 정수
일정한 간격
총 N개의 점
최대 N개의 색깔
모든 색깔에 대해서는 2개 이상의 점이 있음

입력 = 위치 / 색깔
"""

n = int(input())

candidates = [tuple(map(int, input().split())) for _ in range(n)]
# print('candidates', candidates)

answer = 0
max_len = max(c[0] for c in candidates)
# print('max_len', max_len)

for p1 in candidates:
    p1_len = max_len

    for p2 in candidates:
        if p1 == p2:
            continue

        if p1[1] == p2[1]:
            # print(p1, p2)
            p1_len = min(p1_len, abs(p1[0] - p2[0]))

    answer += p1_len

print(answer)