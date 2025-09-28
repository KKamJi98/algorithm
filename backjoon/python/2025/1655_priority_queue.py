# https://www.acmicpc.net/problem/1655 - 가운데를 말해요 (Gold 2)
# Priority_Queue
import sys, heapq
input = sys.stdin.readline

left = []   # 최대 힙 (음수로 저장)
right = []  # 최소 힙
outputs = []

n = int(input())
for _ in range(n):
    x = int(input())
    
    # 1. 왼쪽에 우선 삽입
    if not left or x <= -left[0]:
        heapq.heappush(left, -x)
    else:
        heapq.heappush(right, x)
    
    # 2. 균형 맞추기
    if len(left) > len(right) + 1:
        heapq.heappush(right, -heapq.heappop(left))
    elif len(right) > len(left):
        heapq.heappush(left, -heapq.heappop(right))
    
    # 3. 가운데 값은 왼쪽 힙 루트
    outputs.append(str(-left[0]))

print("\n".join(outputs))