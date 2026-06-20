from itertools import permutations

def solution(a, b):
    
    answer = 0
    n = len(a)
    
    for p in permutations(b, n):
        tmp = 0
        
        for i in range(n):
            tmp += a[i] * p[i]
            # print('tmp', tmp)
    
        answer = min(answer, tmp) if answer != 0 else tmp
        
    return answer