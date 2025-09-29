# https://www.acmicpc.net/problem/7562 - 나이트의 이동 (Silver 1)
# BFS

import sys
from collections import deque

input = sys.stdin.readline

mv = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]


def dfs():
    size = int(input())
    start_row, start_col = map(int, input().split())
    dest_row, dest_col = map(int, input().split())

    board = [[0] * size for _ in range(size)]
    visited = [[False] * size for _ in range(size)]

    q = deque()

    q.append((start_row, start_col, 0))
    board[start_row][start_col] = 0
    visited[start_row][start_col] = True

    while q:
        current_row, current_col, current_dist = q.popleft()
        if current_row == dest_row and current_col == dest_col:
            print(current_dist)
            return

        for dir_row, dir_col in mv:
            next_row, next_col = current_row + dir_row, current_col + dir_col

            if 0 <= next_row < size and 0 <= next_col < size:
                if visited[next_row][next_col] == False:
                    q.append((next_row, next_col, current_dist + 1))
                    visited[next_row][next_col] = True
                    board[next_row][next_col] = current_dist + 1


T = int(input())

for _ in range(T):
    dfs()
