# https://www.acmicpc.net/problem/15651 - [ N과 M ] (3)

def back_tracking(cur_idx, arr_in):
    if cur_idx == M:
        print(*arr_in)
        return
    
    for i in range(1, N + 1):
        arr_in.append(i)
        back_tracking(cur_idx+1, arr_in)
        arr_in.pop()
    

N, M = map(int, input().split())

back_tracking(0, [])