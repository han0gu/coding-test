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
    
    answer = []
    
    for cur_idx, cur_val in enumerate(readings):
        flag = False
        
        for next_idx, next_val in enumerate(readings[cur_idx:]):
            if next_val > cur_val:
                flag = True
                answer.append([next_val, next_idx])
                break
            
        if not flag:
            answer.append([-1, -1])
            
    return answer

if __name__ == '__main__':
    readings_count = int(input().strip())

    readings = []

    for _ in range(readings_count):
        readings_item = int(input().strip())
        readings.append(readings_item)

    result = findNextGreaterElementsWithDistance(readings)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
