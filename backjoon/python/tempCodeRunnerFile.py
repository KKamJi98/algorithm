# https://www.acmicpc.net/problem/15655 - [ N과 M (6) ]
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
input_arr = list(map(int, sys.stdin.readline().rstrip().split()))
input_arr.sort()

arr = []
used = [False] * N
def back_tracking(cur_idx: int, arr_idx):
    if cur_idx == M:
        print(*arr)
        return
    
    for i in range(arr_idx, N):
        # if used[i] == False:
            arr.append(input_arr[i])
            # used[i] = True
            back_tracking(cur_idx + 1, arr_idx + i)
            # used[i] = False
            arr.pop()

back_tracking(0, 0)