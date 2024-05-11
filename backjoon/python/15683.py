# https://www.acmicpc.net/problem/15683 - [ 감시 ]
from collections import deque
import copy
import sys
input = sys.stdin.readline

# 12 -> 3 -> 6 -> 9
cctv_type = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [0, 3]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3],]
}
# print(cctv_type[1])
mv = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # [x, y] 12 -> 3 -> 6 -> 9
board = []
min_area = 0


def check(x_pos, y_pos):
    # print(f"M => {M}\tN => {N}")
    return x_pos >=0 and y_pos >= 0 and x_pos < M and y_pos < N and board[y_pos][x_pos] != 6

def fill(x_pos, y_pos, direct, board_in):
    next_x = x_pos + mv[direct][0]
    next_y = y_pos + mv[direct][1]
    while check(next_x, next_y):
        board_in[next_y][next_x] = -1
        next_x += mv[direct][0]
        next_y += mv[direct][1]
    
#TODO
def watch(cctv_list, board):  # 일자감시 cctv_list => cctv_type, x_pos, y_pos 
    pass
    # 첫번째 꺼 cur = cctv_list.pop() 방향 => for i in range(cctv_type[cur[2]])
        # 채우기 => 함수로 분리 fill(direct)함수 for i in range(cctv_type)
        # 다음꺼 확인 cctv_list.pop() 방향 => cur = for i in range(cctv_type[cur[2]])
        # ... 반복 until cctv_list is empty
    



if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    cctv_list = list()
    for i in range(N):
        for j in range(M):
            if 1 <= board[i][j] and board[i][j] <= 5:
                cctv_list.append([j, i, board[i][j]])  # x_pos, y_pos, cctv_type
            elif board[i][j] == 0:
                min_area += 1
                
    # test
    fill(2, 2, 2, board)
    print()
    for i in range (N):
        print(*board[i])
    print()
    print(cctv_list)