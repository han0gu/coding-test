#!/bin/python3

#
# Complete the 'findTaskPairForSlot' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY taskDurations
#  2. INTEGER slotLength
#
from collections import Counter

def findTaskPairForSlot(taskDurations, slotLength):
    # print('taskDurations', taskDurations)
    # print('slotLength', slotLength)
    
    if len(taskDurations) < 2 or slotLength < 2:
        return [-1, -1]
        
    d = Counter(taskDurations)
    # print('d', d)
    
    for i in range(len(taskDurations) - 1):
        n1 = taskDurations[i]
        n2 = slotLength - n1
        
        if d.get(n2) and d.get(n2) > 0:
            for j in range(i+1, len(taskDurations)):
                if i != j and taskDurations[j] == n2:
                    return [i, j]
            
    return [-1, -1]
    

if __name__ == '__main__':
    taskDurations_count = int(input().strip())

    taskDurations = []

    for _ in range(taskDurations_count):
        taskDurations_item = int(input().strip())
        taskDurations.append(taskDurations_item)

    slotLength = int(input().strip())

    result = findTaskPairForSlot(taskDurations, slotLength)

    print('\n'.join(map(str, result)))
