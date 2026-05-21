"""
총 10개의 입력
각 입력 값 1~100
"""

"""
python3 문제집/완전탐색/2851-슈퍼-마리오/main.py << "EOF"
10
20
30
40
50
60
70
80
90
100
EOF

python3 문제집/완전탐색/2851-슈퍼-마리오/main.py << "EOF"
1
2
3
5
8
13
21
34
55
89
EOF

python3 문제집/완전탐색/2851-슈퍼-마리오/main.py << "EOF"
40
40
40
40
40
40
40
40
40
40
EOF
"""
inputs = [int(input()) for _ in range(10)]
# print("inputs", inputs)

TARGET = 100
answer_under = 0
answer_over = None
for n in inputs:
    if answer_under + n <= TARGET:
        answer_under += n
    else:
        answer_over = answer_under + n
        break

if not answer_over:
    print(answer_under)
else:
    if TARGET - answer_under < answer_over - TARGET:
        print(answer_under)
    else:
        print(answer_over)
