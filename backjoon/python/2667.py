# https://www.acmicpc.net/problem/2667 - [ 단지번호붙이기 ]
import sys
from collections import deque

map_size = int(sys.stdin.readline().rstrip())

my_map = []
for _ in range(map_size):
    my_map.append(list(map(int, sys.stdin.readline().rstrip())))
    
check_map = [[0 for _ in range(map_size)] for _ in range(map_size)]
Q = deque()
area_list = []
mv = [[1,0], [-1,0], [0,-1], [0,1]] #상하좌우
count = 0

for row in range(map_size):
    for col in range(map_size):
        if my_map[row][col] == 1 and check_map[row][col] == 0:
            count += 1
            my_map[row][col] = count
            area = 1
            Q.append((row, col))
            check_map[row][col] = 1 #방문처리 해줌. 방문한 지점은 1로 표시.
            while Q:
                cur_row, cur_col = Q.popleft()
                for mv_row, mv_col in mv:
                    next_row = cur_row + mv_row
                    next_col = cur_col + mv_col
                    if 0 <= next_row < map_size and 0 <= next_col < map_size and my_map[next_row][next_col] == 1 and check_map[next_row][next_col] == 0:
                        Q.append((next_row, next_col))
                        my_map[next_row][next_col] = count
                        check_map[next_row][next_col] = 1
                        area += 1
            area_list.append(area)
        
area_list.sort()
print(len(area_list))
for ele in area_list:
    print(ele)
