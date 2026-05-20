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

import random

dwarfs = [int(input()) for _ in range(9)]

while True:
    flag = False
    answer = []
    random.shuffle(dwarfs)

    for d in dwarfs:
        if sum(answer) + d > 100:
            break

        answer.append(d)
        
        if sum(answer) == 100 and len(answer) == 7:
            flag = True
            break

    if flag:
        answer.sort()
        for i in answer:
            print(i)
        break
    