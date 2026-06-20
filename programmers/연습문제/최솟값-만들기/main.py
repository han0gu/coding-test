def solution(a, b):
    a.sort()
    b.sort(reverse=True)
    
    return sum(x * y for x, y in zip(a, b))