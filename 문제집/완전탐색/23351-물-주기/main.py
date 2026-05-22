"""
n개의 화분
"""
n, k, a, b = map(int, input().split())

flowers = [k] * n
# print('init flowers', flowers)

day = 0
water_start = 0
while 0 not in flowers:
    day += 1

    for i in range(water_start, water_start + a):
        flowers[i] += b

    flowers = [f - 1 for f in flowers]

    # print(day, water_start, flowers)

    water_start = (water_start + a) % n

print(day)

"""
python3 '문제집/완전탐색/23351-물-주기/main.py' << 'EOF'
6 3 2 2
EOF

python3 '문제집/완전탐색/23351-물-주기/main.py' << 'EOF'
2 2 1 1
EOF
"""