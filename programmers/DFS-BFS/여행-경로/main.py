def solution(tickets):
    answer = []
    
    n = len(tickets)
    stack = [('ICN', 0, [False] * n, ['ICN'])] # (도착지, 사용한 티켓 수, 티켓 사용 여부, 정답 리스트)
    
    while stack:
        cur_e, cnt, visited, cur_answer = stack.pop()
        
        if cnt == n:
            answer.append(cur_answer)
            continue
            
        for i, (nxt_s, nxt_e) in enumerate(tickets):
            if not visited[i] and cur_e == nxt_s:
                new_visited = [*visited]
                new_answer = [*cur_answer]
                
                new_visited[i] = True
                new_answer.append(nxt_e)
                
                stack.append( (nxt_e, cnt + 1, new_visited, new_answer) )
    
    return min(answer)
    