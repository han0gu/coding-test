"""
python3 '문제집/완전탐색/2309-일곱-난쟁이/main.py' << 'EOF'
20
7
23
19
10
15
25
8
13
EOF
"""

"""
입력 9명
정답 7명
합 100
무조건 정답 있음
"""
dwarfs = [int(input()) for _ in range(9)]

flag = False
for i in range(9):
    exclude_1 = dwarfs[:i] + dwarfs[i+1:]
    sum_exclude_1 = sum(exclude_1)
    
    for j in range(8):
        if sum_exclude_1 - exclude_1[j] == 100:
            exclude_2 = exclude_1[:j] + exclude_1[j+1:]
            exclude_2.sort()
            
            for d in exclude_2:
                print(d)

            flag = True
            break
    if flag:
        break
