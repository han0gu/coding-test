"""
1 ≤ n ≤ 100,000, 

1 ≤ ai ≤ 1,000,000, 

1 ≤ x ≤ 2,000,000
"""
n = int(input())

numbers = list(map(int, input().split()))
# print('numbers', numbers)

x = int(input())


numbers.sort()
start = 0
end = len(numbers) - 1
answer = 0

while start < end:
    total = numbers[start] + numbers[end]
    if total == x:
        answer += 1
        start += 1
        end -= 1
    elif total < x:
        start += 1
    else:
        end -= 1

print(answer)