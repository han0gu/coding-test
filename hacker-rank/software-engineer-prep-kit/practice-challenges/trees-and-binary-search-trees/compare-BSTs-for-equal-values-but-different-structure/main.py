#!/bin/python3

#
# Complete the 'verifySameMultisetDifferentStructure' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER_ARRAY root1
#  2. INTEGER_ARRAY root2
#

def verifySameMultisetDifferentStructure(root1, root2):

    if not root1 or not root2 or (root1 == root2):
        return 0

    exclude = 100001

    real_idx_1 = []
    real_value_1 = []
    for i, v in enumerate(root1):
        if v != exclude:
            real_idx_1.append(i)
            real_value_1.append(v)

    real_idx_2 = []
    real_value_2 = []
    for i, v in enumerate(root2):
        if v != exclude:
            real_idx_2.append(i)
            real_value_2.append(v)

    return real_idx_1 != real_idx_2 and sorted(real_value_1) == sorted(real_value_2)

if __name__ == '__main__':
    root1_count = int(input().strip())

    root1 = []

    for _ in range(root1_count):
        root1_item = int(input().strip())
        root1.append(root1_item)

    root2_count = int(input().strip())

    root2 = []

    for _ in range(root2_count):
        root2_item = int(input().strip())
        root2.append(root2_item)

    result = verifySameMultisetDifferentStructure(root1, root2)

    print(int(result))
