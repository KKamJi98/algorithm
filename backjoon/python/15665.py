# https://www.acmicpc.net/problem/15665 - [ N과 M (11) ]

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr_in = list(map(int, sys.stdin.readline().split()))
arr_in.sort()

def back_tracking(arr, depth):
  append_val = -1
  
  if depth == M:
    print(*arr)
    return
  
  
  for i in range(N):
    if append_val == arr_in[i]:
      continue

    arr.append(arr_in[i])
    append_val = arr_in[i]
    back_tracking(arr, depth+1)
    arr.pop()
    
back_tracking(deque(), 0) 