n = int(input())
candidates = [tuple(map(int, input().split())) for _ in range(n)]  # need, profit

answer = 0
stack = [(0, 0)]  # nxt_idx, cur_acc

while stack:
    nxt_idx, cur_acc = stack.pop()

    if nxt_idx == n:
        answer = max(answer, cur_acc)
        continue

    nxt_need, nxt_profit = candidates[nxt_idx]

    stack.append((nxt_idx + 1, cur_acc))  # 미선택

    if nxt_idx + nxt_need <= n:
        stack.append((nxt_idx + nxt_need, cur_acc + nxt_profit))  # 선택

print(answer)
