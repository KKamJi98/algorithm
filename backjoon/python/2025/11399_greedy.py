# https://www.acmicpc.net/problem/11399 - ATM (Silver 4)

import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
arr.sort()

waiting_time = 0
total_time = 0

for i in arr:
    total_time += i
    waiting_time += total_time

print(waiting_time)
