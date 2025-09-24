# https://www.acmicpc.net/problem/2583 - [ 영역 구하기 ]
import sys
from collections import deque

row_size, col_size, ract_num = map(int, sys.stdin.readline().rstrip().split())

array = [[-1 for _ in range(col_size)] for _ in range(row_size)]
for _ in range(ract_num):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            array[j][i] = 1

size = []
mv = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for y in range(row_size):
    for x in range(col_size):
        if array[y][x] == -1:
            ract_area = 1
            array[y][x] = 0
            Q = deque([(x, y)])
            while Q:
                cur_x, cur_y = Q.popleft()
                for next in mv:
                    next_x, next_y = cur_x + next[0], cur_y + next[1]
                    if (
                        0 <= next_x < col_size
                        and 0 <= next_y < row_size
                        and array[next_y][next_x] == -1
                    ):
                        array[next_y][next_x] = 0
                        Q.append((next_x, next_y))
                        ract_area += 1
            size.append(ract_area)

size.sort()
print(len(size))
for ele in size:
    print(ele, end=" ")
