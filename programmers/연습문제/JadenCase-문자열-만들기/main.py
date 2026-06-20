def solution(s):
    answer = []
    
    ls = s.split(' ')
    
    for s in ls:
        # 공백 처리
        if not s:
            answer.append('@')
            continue
            
        s = s.lower() # toLower
        s = s[0].upper() + s[1:] # 맨 첫 글자만 대문자로 변경
        answer.append(s)
    
    return ' '.join(answer).replace('@', '')
    