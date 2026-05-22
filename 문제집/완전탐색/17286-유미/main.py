"""
사람 3명

-10 <= x,y <= 10
"""
import math
from itertools import permutations

dot_coordinates = [list(map(int,input().split())) for _ in range(4)]
# print(dot_coordinates)

visit_orders = [[0] + list(order) for order in permutations([1,2,3])]

def calculate_distance(visit_order):
    distance = 0

    for i in range(len(visit_order) - 1):
        cur_dot = visit_order[i]
        next_dot = visit_order[i + 1]
        x_diff = dot_coordinates[cur_dot][0] - dot_coordinates[next_dot][0]
        y_diff = dot_coordinates[cur_dot][1] - dot_coordinates[next_dot][1]
        distance += math.sqrt(x_diff**2 + y_diff**2)

    return distance

distances = []
for vo in visit_orders:
    distances.append(calculate_distance(vo))

# print('distances', distances)
print(int(min(distances)))

"""
python3 '문제집/완전탐색/17286-유미/main.py' << 'EOF'
0 0
1 0
2 0
4 0
EOF
"""