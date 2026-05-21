"""
모든 방에 빈 침대가 없어야 함
모든 종류의 방을 사용하지 않아도 됨, 일부만 사용해도 됨
각 방의 정원 1 ~ 50명
전체 학생 수 1 ~ 300명
"""

a, b, c, n = map(int, input().split())

flag = False

for i in range(n // a + 1):
    for j in range(n // b + 1):
        for k in range(n//c + 1):
            flag = a*i + b*j + c*k == n
            if flag:
                break
        if flag:
            break
    if flag:
        break

print(1 if flag else 0)
