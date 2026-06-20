from collections import Counter


def solution(k, tangerine):
    counts = sorted(Counter(tangerine).values(), reverse=True)

    for answer, count in enumerate(counts, 1):
        k -= count

        if k <= 0:
            return answer

    return answer
