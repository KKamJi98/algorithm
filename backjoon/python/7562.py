# https://www.acmicpc.net/problem/7562 - [ 나이트의 이동 ]
import sys
from collections import deque


def bfs():
    Q = deque()
    chessboard_size = int(sys.stdin.readline().rstrip())
    cur_row, cur_col = list(map(int, sys.stdin.readline().rstrip().split()))
    Q.append([cur_row, cur_col])
    dist = [[-1 for _ in range(chessboard_size)] for _ in range(chessboard_size)]
    dist[cur_row][cur_col] = 0

    dest_row, dest_col = list(map(int, sys.stdin.readline().rstrip().split()))
    mv = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]
    while Q:
        cur_row, cur_col = Q.popleft()
        if cur_row == dest_row and cur_col == dest_col:
            return dist[cur_row][cur_col]
        for next in mv:
            mv_row, mv_col = next
            next_row = cur_row + mv_row
            next_col = cur_col + mv_col
            if (
                next_row < 0
                or next_row >= chessboard_size
                or next_col < 0
                or next_col >= chessboard_size
            ):
                continue

            if dist[next_row][next_col] == -1:
                dist[next_row][next_col] = dist[cur_row][cur_col] + 1
                Q.append([next_row, next_col])

    return dist[dest_row][dest_col]


test_case = int(sys.stdin.readline().rstrip())
for _ in range(test_case):
    print(bfs())
