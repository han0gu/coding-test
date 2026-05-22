numbers = [
['###', '#.#', '#.#', '#.#', '###'], # 0
['..#', '..#', '..#', '..#', '..#'], # 1
['###', '..#', '###', '#..', '###'], # 2
['###', '..#', '###', '..#', '###'], # 3
['#.#', '#.#', '###', '..#', '..#'], # 4
['###', '#..', '###', '..#', '###'], # 5
['###', '#..', '###', '#.#', '###'], # 6
['###', '..#', '..#', '..#', '..#'], # 7
['###', '#.#', '###', '#.#', '###'], # 8
['###', '#.#', '###', '..#', '###'], # 9
]

raw_inputs = [input().split() for _ in range(5)]
# print('raw_inputs', raw_inputs)

input_number_1 = []
input_number_2 = []
input_number_3 = []
input_number_4 = []
for row in range(5):
    input_number_1.append(raw_inputs[row][0])
    input_number_2.append(raw_inputs[row][1])
    input_number_3.append(raw_inputs[row][2])
    input_number_4.append(raw_inputs[row][3])
# print('input_number_1', input_number_1)

def validate(input_number):
    for i in range(10):
        target_number = numbers[i]
        flag = True

        for row in range(5):
            for col in range(3):
                # print('input_number_2[row][col]', input_number_2[row][col])
                # print('target_number[row][col]', target_number[row][col])
                if input_number[row][col] == '#' and target_number[row][col] == '.':
                    flag = False
        # print(i, input_number_2, target_number, flag)

        if flag:
            return str(i)

answer = []
answer.append(validate(input_number_1))
answer.append(validate(input_number_2))
answer.append(validate(input_number_3))
answer.append(validate(input_number_4))
print(f"{''.join(answer[:2])}:{''.join(answer[2:])}")



"""
python3 '문제집/완전탐색/2082-시계/main.py' << 'EOF'
#.# ... ... #..
#.# ... ... #..
#.# ### ### ###
#.# #.. ..# ..#
### ### ### ..#
EOF
"""
