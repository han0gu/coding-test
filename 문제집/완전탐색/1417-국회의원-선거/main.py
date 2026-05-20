"""
python3 '문제집/완전탐색/1417-국회의원-선거/main.py' << 'EOF'
5
5
10
7
3
8
EOF
"""

"""
후보 N명 <= 50
마을 주민 M명 <= 100
"""
candidate_counts = int(input())
# print("candidate_counts", candidate_counts)

# 나 혼자 출마한 경우
if candidate_counts == 1:
    print(0)
# 경쟁자가 있는 경우
else:
    total_tickets = []
    for _ in range(candidate_counts):
        total_tickets.append(int(input()))
    # print("total_tickets", total_tickets)

    cnt = 0
    me = total_tickets[0]
    others = total_tickets[1:]
    while True:
        target_value = max(others)
        
        if me > target_value:
            break

        target_idx = others.index(target_value)
        others[target_idx] = others[target_idx] - 1
        me += 1
        cnt += 1

    print(cnt)