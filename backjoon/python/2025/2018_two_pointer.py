# https://www.acmicpc.net/problem/2018 - 수들의 합 5 (Silver 5)
# Two Pointer - O(n)

n = int(input())

cnt = 0
start, end = 1, 1
total = 1

while start <= n:
    if total == n:
        cnt += 1
        total -= start
        start += 1
    if total < n:
        end += 1
        if end > n:
            break
        total += end
    else: #total > n
        total -= start
        start += 1

print(cnt)