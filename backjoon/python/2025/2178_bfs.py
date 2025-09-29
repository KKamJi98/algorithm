# https://www.acmicpc.net/problem/2178 - 미로 탐색 (Silver 1)
# BFS

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
adj = [list(map(int, input().strip())) for _ in range(N)]
mv = ((-1, 0), (1, 0), (0, -1), (0, 1))


def bfs():
    dist = [[0] * M for _ in range(N)]
    q = deque([(0, 0)])
    dist[0][0] = 1

    while q:
        x, y = q.popleft()
        if x == N - 1 and y == M - 1:
            print(dist[x][y])
            return
        for dx, dy in mv:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if adj[nx][ny] == 1 and dist[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))


bfs()
