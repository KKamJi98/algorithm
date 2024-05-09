# https://www.acmicpc.net/problem/15683 - [ 감시 ]
import copy
import sys; input = sys.stdin.readline
from collections import deque

# 12 -> 3 -> 6 -> 9
cctv_watch = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [0, 3]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3 ,0], [3, 0, 1]],
    5: [[0, 1, 2, 3],]
}

mv = [[0, 1], [1, 0], [0,-1], [-1, 0]] # [x, y] 12 -> 3 -> 6 -> 9

board = []
min_area = 0

def check(x_pos, y_pos):
    return x_pos < 0 or y_pos >= N or x_pos >= M or y_pos < 0

def watch(cctv_info, board): # 일자감시 cctv_info => cctv_type, x_pos, y_pos
    

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    cctv_info = list()
    for i in range(N):
        for j in range(M):
            if 1 <= board[i][j] and board[i][j] <= 5:
                cctv_info.append(j, i, board[i][j]) # x_pos, y_pos, cctv_type
            elif board[i][j] == 0:
                min_area += 1
    