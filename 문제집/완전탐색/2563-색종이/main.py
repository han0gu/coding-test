"""
python3 '문제집/완전탐색/2563-색종이/main.py' << 'EOF'
3
3 7
15 7
5 2
EOF
"""

# inputs 파싱
number_of_paper = int(input())

papers = []
for _ in range(number_of_paper):
    x, y = map(int, input().split())
    papers.append((x, y))
# print(">>> papers", papers)


# 100 x 100 2D array
matrix = [[0] * 100 for _ in range(100)]


# paint 함수
def paint(x, y):
    # for x ~ x+9
    for i in range(x, x + 10):
        # paint y ~ y+9, 색칠되어 있지 않은 경우만
        for j in range(y, y + 10):
            if matrix[i][j] == 0:
                matrix[i][j] = 1


# paint 실행
for x, y in papers:
    paint(x, y)

# 정답 계산
answer = 0
for i in range(100):
    answer += sum(matrix[i])
print(answer)
