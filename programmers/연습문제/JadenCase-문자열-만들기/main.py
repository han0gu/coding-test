def solution(s):
    answer = []
    
    words = s.split(' ')
    
    for w in words:
        if w:
            w = w.lower()
            w = w[0].upper() + w[1:]
        
        answer.append(w)
        
    return ' '.join(answer)
    