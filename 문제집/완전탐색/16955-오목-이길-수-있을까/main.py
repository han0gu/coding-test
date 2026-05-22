"""
바둑판 10x10

주인공: X
상대방: O
"""
ROW_MAX = 10
COL_MAX = 10
board = [input() for _ in range(ROW_MAX)]
flag = False

def validate_candidates(candidates):
    # `O`가 없고 `X`가 4개 이상
    if 'O' not in candidates and candidates.count('.') <= 1:
        global flag
        flag = True

def check_0(row, col):
    # 지정된 방향으로 5개 확인 ->
    if row + 4 < ROW_MAX:
        candidates = [board[row + i][col] for i in range(5)]
        # print('candidates',candidates)
        validate_candidates(candidates)

def check_45(row, col):
    # 지정된 방향으로 5개 확인 ->
    if row - 4 >= 0 and col + 4 < COL_MAX:
        candidates = [board[row - i][col + i] for i in range(5)]
        # print('candidates',candidates)
        validate_candidates(candidates)

def check_90(row, col):
    # 지정된 방향으로 5개 확인 ->
    if col + 4 < COL_MAX:
        candidates = [board[row][col + i] for i in range(5)]
        # print('candidates',candidates)
        validate_candidates(candidates)

def check_135(row, col):
    # 지정된 방향으로 5개 확인 ->
    if row + 4 < ROW_MAX and col + 4 < COL_MAX:
        candidates = [board[row + i][col + i] for i in range(5)]
        # print('candidates',candidates)
        validate_candidates(candidates)

for row in range(10):
    for col in range(10):
        check_0(row, col)
        check_45(row, col)
        check_90(row, col)
        check_135(row, col)

        if flag:
            break

    if flag:
        break

print(1 if flag else 0)

"""
python3 '문제집/완전탐색/16955-오목-이길-수-있을까/main.py' << 'EOF'
XX.XX.....
.....OOOO.
..........
..........
..........
..........
..........
..........
..........
..........
EOF

python3 '문제집/완전탐색/16955-오목-이길-수-있을까/main.py' << 'EOF'
XXOXX.....
OO.O......
..........
..........
..........
..........
..........
..........
..........
..........
EOF
"""
