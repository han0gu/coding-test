"""
테스트 케이스의 개수 N (1 < N < 100)

양의 정수 M (1 < M < 100)개가 주어진다

모든 수는 `-2^31`보다 크거나 같고, `2^31 - 1`보다 작거나 같다. 
"""
import math

n = int(input())
test_cases = [list(map(int, input().split())) for _ in range(n)]
# print('test_cases', test_cases)

def get_d(n) -> list:
    d = []
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            d.append(i)
            d.append(n // i)
    return d
# print(get_d(10))
# print(get_d(20))

def get_gcd(n1, n2):
    gcd = 1
    d1 = sorted(get_d(n1), reverse=True)
    d2 = sorted(get_d(n2), reverse=True)

    target_d = d1 if n1 < n2 else d2
    target_n = max(n1, n2)

    for d in target_d:
        if target_n % d == 0:
            gcd = d
            break

    return gcd

for case in test_cases:
    answer = 1
    
    for i in range(len(case)):
        for j in range(i + 1, len(case)):
            answer = max(answer, get_gcd(case[i], case[j]))

    print(answer)

"""
1
125 15 25

"""