n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
# print('maps', maps)

answer = 0
houses = [] # 모든 집의 좌표 (x,y) 리스트
chicks = [] # 모든 치킨집의 좌표 (x,y) 리스트
for i in range(n):
    for j in range(n):
        cur = maps[i][j]
        if cur == 1:
            houses.append((i,j))
        if cur == 2:
            chicks.append((i,j))
# print('houses', houses)
# print('chicks', chicks)

def get_chick_distance(c_x, c_y, h_x, h_y):
    return abs(c_x - h_x) + abs(c_y - h_y)

def update_chick_distance(chick_idx, house_chick_distance):
    c_x, c_y = chicks[chick_idx]
    new_house_chick_distance = []

    for i, (h_x, h_y) in enumerate(houses):
        new_d = get_chick_distance(c_x, c_y, h_x, h_y)
        new_house_chick_distance.append(min(new_d, house_chick_distance[i]))

    return new_house_chick_distance

# init stack
# 선택한 치킨집에 따른 `도시의 치킨거리` 백트래킹
# (고려한 치킨집 인덱스, 현재까지 선택한 치킨집의 수, 모든 집의 치킨거리 리스트)
init_chick_distances = [2 * n] * len(houses)
stack = [
    (0, 0, init_chick_distances), 
    (0, 1, update_chick_distance(0, init_chick_distances)) 
    ]
# print('init stack', stack)
        
# 
while stack:
    chick_idx, selected_count, chick_distances = stack.pop()

    if chick_idx == len(chicks) - 1 or selected_count == m:
        answer = min(answer, sum(chick_distances)) if answer != 0 else sum(chick_distances)
        continue

    # 다음 치킨집 미선택
    stack.append((chick_idx + 1, selected_count, chick_distances))

    # 다음 치킨집 선택
    stack.append((chick_idx + 1, selected_count + 1, update_chick_distance(chick_idx + 1,chick_distances)))

print(answer)