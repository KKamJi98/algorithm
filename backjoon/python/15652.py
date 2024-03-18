# https://www.acmicpc.net/problem/15652 - [ N과 M (4) ]

arr = []

def back_tracking(cur_idx, last):
    if cur_idx == M:
        print(*arr)
        return
    
    for i in range(last, N+1):
        arr.append(i)
        back_tracking(cur_idx+1, i)
        arr.pop()
        


N, M = map(int, input().split())
back_tracking(0, 1)