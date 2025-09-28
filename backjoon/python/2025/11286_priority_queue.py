# https://www.acmicpc.net/problem/11286 - 절댓값 힙 (Silver 1)
# Priority_Queue
import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []  # (abs(x), x)

out_lines = []
for _ in range(n):
    a = int(input())
    if a == 0:
        if heap:
            out_lines.append(str(heapq.heappop(heap)[1]))
        else:
            out_lines.append("0")
    else:
        heapq.heappush(heap, (abs(a), a))

print("\n".join(out_lines))
