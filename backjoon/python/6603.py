# https://www.acmicpc.net/problem/6603 - [ 로또 ]
import sys

def solutions(depth, idx):
    if depth == 6:
        print(*output_arr)
        return
    
    for i in range(idx, k):
        output_arr.append(arr[i])
        solutions(depth+1, i+1)
        output_arr.pop()

while True:    
    test_case = list(map(int, sys.stdin.readline().rstrip().split()))
    k, arr, output_arr = test_case[0], test_case[1:], []
    if k == 0:
        break
    solutions(0, 0)
    print()
