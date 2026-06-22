def solution(elements):
    answer = []
    
    n = len(elements)
    new_elements = elements * 2
    
    for i in range(1, n+1):
        for j in range(n):
            answer.append(sum(new_elements[j:j+i]))
    
    return len(set(answer))