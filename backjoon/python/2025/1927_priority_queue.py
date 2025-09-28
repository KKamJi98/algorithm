# https://www.acmicpc.net/problem/1927 - 최소 힙 (Silver 2)
# Priority_Queue

import heapq
import sys

input = sys.stdin.readline

n = int(input().strip())

outputs = []
min_heap = []

for _ in range (n):
    input_number = int(input().strip())
    
    if input_number == 0:
        if not min_heap:
            outputs.append('0')
        else:
            outputs.append(str(heapq.heappop(min_heap)))
    else:
        heapq.heappush(min_heap, input_number)
        
print("\n".join(outputs))