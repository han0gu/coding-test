from collections import deque

def solution(progresses, speeds):
    answer = []
    
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    # while 작업 Q에 원소가 남아 있는 동안
    while progresses:
        # 모든 작업에 대해 speed 만큼 진행
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        # head가 100 이상인 경우
        if progresses[0] >= 100:
            pop_cnt = 0
            
            while progresses and progresses[0] >= 100:
                # head 포함 100 이상인 모든 원소를 popleft
                pop_cnt += 1
                
                progresses.popleft()
                speeds.popleft()

            answer.append(pop_cnt)
            
    return answer