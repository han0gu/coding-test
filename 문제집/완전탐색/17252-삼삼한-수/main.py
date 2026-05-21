"""
1 <= N <= 2,147,483,647
각 수를 한번씩만 더해야 함
"""
"""
python3 '문제집/완전탐색/17252-삼삼한-수/main.py' << 'EOF'
109
EOF

python3 '문제집/완전탐색/17252-삼삼한-수/main.py' << 'EOF'
298
EOF
"""

n = int(input())

answer_count = 0

def check(cur_pow, is_added, accumulated_sum):
    cur_num = 3 ** cur_pow
    
    if cur_num > n:
        return
    
    if is_added:
        accumulated_sum += cur_num

        if accumulated_sum < n:
            check(cur_pow + 1, True, accumulated_sum)
            check(cur_pow + 1, False, accumulated_sum)
        if accumulated_sum == n:
            global answer_count
            answer_count += 1
    else:
        check(cur_pow + 1, True, accumulated_sum)
        check(cur_pow + 1, False, accumulated_sum)

check(0, True, 0)
check(0, False, 0)

print('YES' if answer_count > 0 else 'NO')