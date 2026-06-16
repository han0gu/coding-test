from collections import deque

def solution(priorities, location):
    sorted_priorities = deque(sorted(priorities, reverse=True)) # 작업 우선 순위 판단
    process_q = deque((i, p) for i, p in enumerate(priorities)) # 작업 Q
    # print('p_q', p_q, sorted_priorities)
    
    
    # 작업이 남은 동안
    order = 0
    while process_q:
        # 하나 꺼냄
        i, p = process_q.popleft()
        
        # 최우선 순위인 경우
        if p == sorted_priorities[0]:
            # 완료 처리
            order += 1
            sorted_priorities.popleft()
            
            # 원하는 답인 경우 return
            if i == location:
                return order
        # 아닌 경우
        else:
            # 다시 넣음
            process_q.append((i, p))