import heapq

# ver1 heappush, heappop 불가
max_heap = [5, 3, 9, 4, 1, 2, 6]
heapq._heapify_max(max_heap)
print(max_heap)

# ver2, heappush, heappop 가능 (trick 사용)
max_heap = [5, 3, 9, 4, 1, 2, 6]
max_heap = [i * -1 for i in max_heap]
heapq.heapify(max_heap)
print(max_heap)
weight = heapq.heappop(max_heap)
value = -1 * weight

# ver3
max_heap = [5, 3, 9, 4, 1, 2, 6]
max_heap = [(-1 * i, i) for i in max_heap]
heapq.heapify(max_heap)
weight, value = heapq.heappop(max_heap)
print(f"weight={weight}, value={value}")
