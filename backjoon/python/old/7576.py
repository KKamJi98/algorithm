# https://www.acmicpc.net/problem/7576 - [ 토마토 ]
from collections import deque
import sys

col, row = map(int, sys.stdin.readline().rstrip().split())

tomatos = []
dist = [[-1 for _ in range(col)] for _ in range(row)]

for _ in range(row):
    tomatos.append(list(map(int, sys.stdin.readline().rstrip().split())))
Q = deque()
for r in range(len(tomatos)):
    for c in range(len(tomatos[r])):
        if tomatos[r][c] == 1:
            Q.append((r, c))
            dist[r][c] = 0
days = 0

while Q:
    mv = [[1, 0], [-1, 0], [0, -1], [0, 1]]
    curRow, curCol = Q.popleft()
    for mvRow, mvCol in mv:
        nextRow = curRow + mvRow
        nextCol = curCol + mvCol
        if (
            nextRow < 0
            or nextRow >= row
            or nextCol < 0
            or nextCol >= col
            or tomatos[nextRow][nextCol] != 0
        ):
            continue
        Q.append((nextRow, nextCol))
        tomatos[nextRow][nextCol] = 1
        dist[nextRow][nextCol] = dist[curRow][curCol] + 1
        if dist[nextRow][nextCol] > days:
            days = dist[nextRow][nextCol]

for r in tomatos:
    for c in r:
        if c == 0:
            print(-1)
            sys.exit()
print(days)
