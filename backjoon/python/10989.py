# https://www.acmicpc.net/problem/10989 - [ 수 정렬하기 3 ]
import sys

n: int = int(sys.stdin.readline().rstrip("\n"))
arr: list[int] = [0] * (10000 + 1)

lastIdx = 0
for _ in range(n):
    value = int(sys.stdin.readline().rstrip("\n"))
    arr[value] += 1
    if value > lastIdx:
        lastIdx = value

for i in range(lastIdx + 1):
    if arr[i] == 0:
        continue
    else:
        for _ in range(arr[i]):
            print(i)
