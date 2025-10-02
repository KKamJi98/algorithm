# https://www.acmicpc.net/problem/1931 - 회의실 배정 (Gold 5)
# Greedy
import sys

input = sys.stdin.readline

n = int(input())
meet = [tuple(map(int, input().split())) for _ in range(n)]

meet.sort(key=lambda x: (x[1], x[0]))
cnt = 0
end = -1

for cur_start, cur_end in meet:
    if cur_start >= end:
        end = cur_end
        cnt += 1

print(cnt)
