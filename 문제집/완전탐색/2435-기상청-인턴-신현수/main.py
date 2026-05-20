"""
python3 '문제집/완전탐색/2435-기상청-인턴-신현수/main.py' << 'EOF'
2 1
-1 1
EOF
"""

"""
전체 측정 횟수 2 ~ 100
연속 합 길이 1 ~ 100
"""
n, k = map(int, input().split())
temperatures = list(map(int, input().split()))
# print("temperatures", temperatures)

max = -101
for i in range(n-k+1):
    temp_sum = sum(temperatures[i:i+k])
    if max < temp_sum:
        max = temp_sum

print(max)