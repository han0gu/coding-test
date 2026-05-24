#!/bin/python3

#
# Complete the 'getTopKFrequentEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY events
#  2. INTEGER k
#

def getTopKFrequentEvents(events, k):

    if not events or k == 0:
        return []

    event_count = {}
    first_seen_index = {}

    for i, e in enumerate(events):
        if e not in event_count:
            event_count[e] = 1
            first_seen_index[e] = i
        else:
            event_count[e] += 1

    sorted_events = sorted(event_count, key=lambda e: (-event_count[e], first_seen_index[e]))

    return sorted_events[:k]

if __name__ == '__main__':
    events_count = int(input().strip())

    events = []

    for _ in range(events_count):
        events_item = int(input().strip())
        events.append(events_item)

    k = int(input().strip())

    result = getTopKFrequentEvents(events, k)

    print('\n'.join(map(str, result)))
