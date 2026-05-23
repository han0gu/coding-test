#!/bin/python3

#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#

def isAlphabeticPalindrome(code):
    length = len(code)
    if length == 0:
        return 0

    if length == 1:
        return 1

    filtered = [c.lower() for c in code if 'a' <= c <= 'z' or 'A' <= c <= 'Z']
    # print('filtered', filtered)

    mid = len(filtered) // 2
    arr1 = filtered[:mid]
    arr2 = filtered[mid:]
    arr2.reverse()
    # print(arr1, arr2)
    for i in range(mid):
        if arr1[i] != arr2[i]:
            return 0

    return 1


if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
