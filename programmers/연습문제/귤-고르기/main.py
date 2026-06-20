from collections import Counter

def solution(k, tang):
    c = Counter(tang)
    
    ls = []
    for key in c:
        ls.append((key, c[key]))
    ls.sort(key=lambda x: -x[1])
    
    idx = 0
    target_cnt = k
    while True:
        _, value = ls[idx]
        
        if value >= target_cnt:
            return idx + 1
        
        target_cnt -= value
        idx += 1