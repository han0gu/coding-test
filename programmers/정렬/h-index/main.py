def solution(citations):
    n = len(citations)
    citations.sort(reverse=True)

    for i in range(n, 0, -1):
        if citations[i-1] >= i:
            return i

    return 0
