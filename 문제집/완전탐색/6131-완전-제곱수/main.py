"""
python3 '문제집/완전탐색/6131-완전-제곱수/main.py' << 'EOF'
15
EOF
"""

"""
1 ≤ B ≤ A ≤ 500

A^2 = B^2 + N (1 ≤ N ≤ 1,000)
"""

n = int(input())

LIMIT = 500
answer_count = 0
for b in range(1, LIMIT + 1):
    a_square = b**2 + n
    
    if (a_square ** 0.5) % 1 == 0 and a_square <= LIMIT**2:
        answer_count += 1

print(answer_count)