# https://www.acmicpc.net/problem/15654 - [ N과 M (5) ]

def back_tracking(cur_idx, cur_arr, arr_in):
    if cur_idx == M:
        print(*cur_arr)
        return
    
    for i in range(0, N):
        if used[i] == False:
            cur_arr.append(arr_in[i])
            used[i] = True
            back_tracking(cur_idx+1, cur_arr, arr_in)
            used[i] = False
            cur_arr.pop()
        

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
used = [False] * (N + 1)
back_tracking(0, [], arr)