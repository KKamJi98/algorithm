# https://www.acmicpc.net/problem/15663 - [ N과 M (9) ]
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
input_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
tmp_list = []
used = [False] * N

def back_tracking(list_idx:int):
    check = -1
    if len(tmp_list) == M:
        print(*tmp_list)
        return
    
    for i in range(N):
        if used[i] == False and check != input_list[i]:
            tmp_list.append(input_list[i])
            used[i] = True
            check = input_list[i]
            back_tracking(list_idx+1)
            used[i] = False
            tmp_list.pop()
            
back_tracking(0)