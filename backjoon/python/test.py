import sys
from collections import deque

map_size = int(input().strip())

my_map = []
for _ in range(map_size):
    my_map.append(list(map(int, input().strip())))

check_map = [[0 for _ in range(map_size)] for _ in range(map_size)]
Q = deque()
mv = [[1, 0], [-1, 0], [0, -1], [0, 1]]  # 상하좌우
area_list = []

for i in range(map_size):
    for j in range(map_size):
        if my_map[i][j] == 1 and check_map[i][j] == 0:
            area = 1
            Q.append((i, j))
            check_map[i][j] = 1
            
            while Q:
                cur_row, cur_col = Q.popleft()
                for mv_row, mv_col in mv:
                    next_row, next_col = cur_row + mv_row, cur_col + mv_col
                    if 0 <= next_row < map_size and 0 <= next_col < map_size:
                        if my_map[next_row][next_col] == 1 and check_map[next_row][next_col] == 0:
                            Q.append((next_row, next_col))
                            check_map[next_row][next_col] = 1
                            area += 1
            area_list.append(area)

area_list.sort()
print(len(area_list))
for area in area_list:
    print(area)
