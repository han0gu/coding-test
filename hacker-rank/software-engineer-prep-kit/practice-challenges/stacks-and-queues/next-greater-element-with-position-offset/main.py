#!/bin/python3

#
# Complete the 'findNextGreaterElementsWithDistance' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY readings as parameter.
#

def findNextGreaterElementsWithDistance(readings):
    # print('readings', readings)

    if len(readings) < 2:
        return [[-1,-1]]

    answer = [[-1, -1] for _ in range(len(readings))]
    # print('answer', answer)

    stack = []
    for cur_idx, cur_value in enumerate(readings):
        while stack and readings[stack[-1]] < cur_value:
            prev_idx = stack.pop()
            answer[prev_idx] = [cur_value, cur_idx - prev_idx]

        stack.append(cur_idx)
        # print('stack', stack)

    return answer

if __name__ == '__main__':
    readings_count = int(input().strip())

    readings = []

    for _ in range(readings_count):
        readings_item = int(input().strip())
        readings.append(readings_item)

    result = findNextGreaterElementsWithDistance(readings)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
