from collections import deque

def solution(priorities, location):
    priorities_q = deque(sorted(priorities, reverse=True)) # 작업 우선 순위 판단
    priorities_processed = [-1] * len(priorities) # 작업 완료 여부 판단
    # print('priorities_q', priorities_q, priorities_processed)
    
    # 작업이 남은 동안
    order = 1
    while priorities_q:
        # priorities를 순회하면서
        for i, v in enumerate(priorities):
            # 현재 작업 미완료 상태이고 priorities_q의 head와 같은 경우
            if priorities_processed[i] == -1 and v == priorities_q[0]:
                # 실행 처리
                priorities_processed[i] = order
                order += 1
                priorities_q.popleft()
            # else
                # continue
                
    # answer = priorities_processed에서 location 찾기
    # print(priorities_processed)
    return priorities_processed[location]