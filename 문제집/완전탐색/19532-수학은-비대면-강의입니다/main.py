"""
-999 ~ 999 정수
"""
"""
python3 '문제집/완전탐색/19532-수학은-비대면-강의입니다/main.py' << 'EOF'
1 3 -1 4 1 7
EOF

python3 '문제집/완전탐색/19532-수학은-비대면-강의입니다/main.py' << 'EOF'
2 5 8 3 -4 -11
EOF

"""

a,b,c,d,e,f = map(int, input().split())

flag = False
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            flag = True
            print(f"{x} {y}")
        
        if flag:
            break
    
    if flag:
        break