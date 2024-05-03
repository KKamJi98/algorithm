# https://www.acmicpc.net/problem/15666 - [ N과 M (12) ]
# python의 set 자료형을 쓰는 것 이 조금 더 효율적이었을 것임.

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
last_pop = -1
arr = deque()

def solutions(depth, start):
    global last_pop
    if depth == m:
        print(*arr)
        return
        
    for i in range(start, len(numbers)):
        if last_pop == numbers[i]:
            continue
        arr.append(numbers[i])
        solutions(depth + 1, i)
        last_pop = arr.pop()

solutions(0, 0)