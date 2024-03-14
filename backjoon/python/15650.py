import sys

def back_tracking(cur_idx: int, arr_in: list):
    if cur_idx == M:
        print(*arr_in)
        return

    for i in range(1, N+1):
        if arr_in and i < arr_in[-1]:  # arr_in이 비어있지 않을 때만 마지막 요소와 비교
            continue
        if used[i] == False:
            arr_in.append(i)
            used[i] = True
            back_tracking(cur_idx + 1, arr_in)
            used[i] = False
            arr_in.pop()


N, M = map(int, sys.stdin.readline().rstrip().split())
used = [False] * (N +1)
back_tracking(0, [])
