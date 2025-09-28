# https://www.acmicpc.net/problem/3273 - 두 수의 합 (Silver 3)
# Two Pointer - O(n)

n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

cnt = 0
l, r = 0, n - 1

while l < r:
    s = arr[l] + arr[r]
    if s == x:
        cnt += 1
        l += 1
        r -= 1
    elif s < x:
        l += 1
    else:
        r -= 1

print(cnt)
