# https://www.acmicpc.net/problem/1966 - 프린터 큐  - (Silver 3)
# Priority_Queue

import sys, heapq
from collections import deque

input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().strip().split())
    test_arr = list(map(int, input().strip().split()))

    q = deque([(i, p) for i, p in enumerate(test_arr)])

    max_heap = [-p for p in test_arr]
    heapq.heapify(max_heap)

    count = 0

    while q:
        idx, priority = q.popleft()

        if priority == -max_heap[0]:
            heapq.heappop(max_heap)
            count += 1
            if idx == m:
                print(count)
                break
        else:
            q.append((idx, priority))
