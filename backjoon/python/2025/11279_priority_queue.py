# https://www.acmicpc.net/problem/11279 - 최대 힙 (Silver 2)
# Priority_Queue

import heapq
import sys

input = sys.stdin.readline

n = int(input().strip())

max_heap = []
outputs = []
for _ in range (n):
    input_number = int(input().strip())
    if input_number == 0:
        if not max_heap:
            outputs.append('0')
            continue
            
        outputs.append(str(abs(heapq.heappop(max_heap))))
    else:
        heapq.heappush(max_heap, -input_number)
        
print("\n".join(outputs))
