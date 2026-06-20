"""
3
-> 1에서 +2
-> 2에서 +1

4
-> 3에서 +1
-> 2에서 +2
"""
def solution(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, (a + b) % 1234567

    return b
