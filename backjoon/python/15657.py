# https://www.acmicpc.net/problem/15657 - [ N과 M (8) ]
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr_in = list(map(int,sys.stdin.readline().rstrip().split()))
arr_in.sort()
arr = []

def back_tracking(arr_idx):
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(arr_idx, N):
        arr.append(arr_in[i])
        back_tracking(i)
        arr.pop()
        
back_tracking(0)