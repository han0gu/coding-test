from itertools import combinations

def solution(nums):
    comb = combinations(nums, len(nums) // 2)
    print('comb', comb)
    
    # for c in comb:
    #     print(c)
        
    set_1 = set(comb)
    # print('set_1', set_1)
    
    set_2 = [set(s) for s in set_1]
    # print('set_2', set_2)
    
    set_3 = sorted(set_2, key=lambda x: -len(x))
    # print('set_3', set_3)
    
    return len(set_3[0])