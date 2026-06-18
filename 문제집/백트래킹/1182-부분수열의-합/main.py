import sys


def main():
    input = sys.stdin.readline

    n, target = map(int, input().split())
    nums = list(map(int, input().split()))

    answer = 0
    stack = [(0, 0, 0)]  # (index, current_sum, selected_count)

    while stack:
        idx, value, count = stack.pop()

        if idx == n:
            if value == target and count > 0:
                answer += 1
            continue

        stack.append((idx + 1, value + nums[idx], count + 1))
        stack.append((idx + 1, value, count))

    print(answer)


if __name__ == "__main__":
    main()
