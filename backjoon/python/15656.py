# https://www.acmicpc.net/problem/15656 - [ N과 M (7) ]
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
input_arr = list(map(int, sys.stdin.readline().rstrip().split()))
input_arr.sort()

arr = []


def back_tracking(arr_idx):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(N):
        arr.append(input_arr[i])
        back_tracking(arr_idx + 1)
        arr.pop()


back_tracking(0)
