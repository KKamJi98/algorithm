# https://www.acmicpc.net/problem/15664 - [N과 M (10)]

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
arr_in = list(map(int, sys.stdin.readline().rstrip().split()))
arr_in.sort()

def back_tracking(arr, depth, last_idx):
  append_val = -1
  if depth == M:
    print(*arr)
    return

  for i in range(last_idx, N):
    if (arr_in[i] == append_val):
      continue
    arr.append(arr_in[i])
    append_val = arr_in[i]
    back_tracking(arr, depth + 1, i + 1)
    arr.pop()

back_tracking(deque(), 0, 0)