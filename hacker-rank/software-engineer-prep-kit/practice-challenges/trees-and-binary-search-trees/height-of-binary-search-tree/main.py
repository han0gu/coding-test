#!/bin/python3

#
# Complete the 'getBinarySearchTreeHeight' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY leftChild
#  3. INTEGER_ARRAY rightChild
#

from collections import deque

def getBinarySearchTreeHeight(values, leftChild, rightChild):
    # print('values', values)
    # print('leftChild', leftChild)
    # print('rightChild', rightChild)

    if len(values) <= 1:
        return len(values)

    queue = deque()
    queue.append((0, 1)) # idx, depth
    answer = 1
    while queue:
        i, depth = queue.popleft()
        answer = max(answer, depth)

        if leftChild[i] != -1:
            queue.append((leftChild[i], depth + 1))
        if rightChild[i] != -1:
            queue.append((rightChild[i], depth + 1))

    return answer


if __name__ == '__main__':
    values_count = int(input().strip())

    values = []

    for _ in range(values_count):
        values_item = int(input().strip())
        values.append(values_item)

    leftChild_count = int(input().strip())

    leftChild = []

    for _ in range(leftChild_count):
        leftChild_item = int(input().strip())
        leftChild.append(leftChild_item)

    rightChild_count = int(input().strip())

    rightChild = []

    for _ in range(rightChild_count):
        rightChild_item = int(input().strip())
        rightChild.append(rightChild_item)

    result = getBinarySearchTreeHeight(values, leftChild, rightChild)

    print(result)
