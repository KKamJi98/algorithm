# https://www.acmicpc.net/problem/1012 - 유기농 배추 (Silver 2)
# BFS

import sys
from collections import deque

input = sys.stdin.readline

mv = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(start_x, start_y, adj):
    current_x = start_x
    current_y = start_y

    q = deque([(current_y, current_x)])
    adj[current_y][current_x] = 0

    while q:
        current_y, current_x = q.popleft()

        for dir in mv:
            next_y, next_x = current_y + dir[0], current_x + dir[1]
            if 0 <= next_y < N and 0 <= next_x < M and adj[next_y][next_x] == 1:
                adj[next_y][next_x] = 0
                q.append((next_y, next_x))


test_case = int(input())

for _ in range(test_case):
    M, N, K = map(int, input().split())

    adj = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        adj[y][x] = 1

    count = 0
    for row in range(N):
        for col in range(M):
            if adj[row][col] == 1:
                bfs(col, row, adj)
                count += 1
    print(count)
