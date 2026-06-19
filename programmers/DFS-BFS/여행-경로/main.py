from collections import deque

def solution(tickets):
    answer = []
    n = len(tickets)
    
    q = deque([('ICN', 0, [], ['ICN'])]) # (도착지, 검토할 티켓 인덱스, 이미 검토한 티켓 인덱스 리스트, answer)
    
    while q:
        cur_e, idx, visited_idx, cur_answer = q.popleft()
        
        if idx == n:
            answer.append(cur_answer)
        
        for i, (nxt_s, nxt_e) in enumerate(tickets):
            if i not in visited_idx and cur_e == nxt_s:
                new_visited_idx = [*visited_idx]
                new_answer = [*cur_answer]
                
                new_visited_idx.append(i)
                new_answer.append(nxt_e)
                
                q.append( (nxt_e, idx + 1, new_visited_idx, new_answer) )
                
    
    if len(answer) == 1:
        return answer[0]
    else:
        answer.sort()
        return answer[0]