# https://www.acmicpc.net/problem/15649 - [ N과 M (1) ]
import sys
from collections import deque


def backTracking(cur_idx: int):
    if cur_idx == M:
        print(*arr)
        return

    for i in range(1, N + 1):
        if not check[i]:
            arr.append(i)
            check[i] = True
            backTracking(cur_idx + 1)
            check[i] = False
            arr.pop()


N, M = map(int, sys.stdin.readline().rstrip().split())
arr = []
check = [False] * (N + 1)
backTracking(0)
