# https://www.acmicpc.net/problem/2667 - 단지번호붙이기 (Silver 1)

import sys
from collections import deque

input = sys.stdin.readline

mv = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(start_row, start_col, adj, visited):
    H, W = len(adj), len(adj[0])
    q = deque([(start_row, start_col)])
    visited[start_row][start_col] = True
    size = 1

    while q:
        current_row, current_col = q.popleft()
        for dr, dc in mv:
            next_row, next_col = current_row + dr, current_col + dc
            if 0 <= next_row < H and 0 <= next_col < W:
                if (
                    adj[next_row][next_col] == 1
                    and visited[next_row][next_col] == False
                ):
                    q.append((next_row, next_col))
                    visited[next_row][next_col] = True
                    size += 1

    return size


N = int(input())

adj = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

sizes = []
for row in range(N):
    for col in range(N):
        if adj[row][col] == 1 and visited[row][col] == False:
            sizes.append(bfs(row, col, adj, visited))

print(len(sizes))
for size in sorted(sizes):
    print(size)
