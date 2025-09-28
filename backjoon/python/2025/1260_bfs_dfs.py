# https://www.acmicpc.net/problem/1260 - DFS와 BFS
# DFS, BFS

import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(1_000_000)

N, M, V = map(int, input().split())

adj = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(1, N + 1):
    if adj[i]:
        adj[i] = sorted(set(adj[i]))

visited = [False] * (N + 1)
dfs_order = []


def dfs(v: int):
    visited[v] = True
    dfs_order.append(v)
    for nv in adj[v]:
        if not visited[nv]:
            dfs(nv)


dfs(V)


def bfs(start: int):
    visited = [False] * (N + 1)
    q = deque([start])
    visited[start] = True
    order = []

    while q:
        v = q.popleft()
        order.append(v)
        for nv in adj[v]:
            if not visited[nv]:
                visited[nv] = True
                q.append(nv)

    return order


bfs_order = bfs(V)

print(*dfs_order)
print(*bfs_order)
