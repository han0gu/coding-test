"""
python3 '문제집/완전탐색/14568-2017-연세대학교-프로그래밍-경시대회/main.py' << 'EOF'
7
EOF
"""

"""
총 사탕 수 N = 1~100

모두 자연수 개의 사탕을 받음

택희(a) = 짝수(최소 2개)
남규(c) >= 영훈(b) + 2
"""
n = int(input())

if n < 6:
    print(0)
elif n == 6:
    print(1)
else:
    answer_count = 0

    # 택희(a) 먼저 결정
    for a in range(2, n, 2):
        exclude_a = n - a

        # 영훈(b)
        for b in range(1, exclude_a):
            # 남규(c)
            c = exclude_a - b

            if c >= b + 2:
                answer_count += 1

    print(answer_count)
