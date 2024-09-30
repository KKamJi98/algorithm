import heapq

# parent node = (i-1) // 2
# child node = [left]2 * i + 1, [right]2 * i + 2
min_heap = [5, 3, 9, 4, 1, 2, 6]

# heapify => O(N)
heapq.heapify(min_heap)
print(min_heap)  # [1, 3, 2, 4, 5, 9, 6]

# Sift Down => O(logN)
print(heapq.heappop(min_heap))  # 1
print(min_heap)  # [2, 3, 6, 4, 5, 9]

# Sift Up => O(logN)
heapq.heappush(min_heap, 1)
print(min_heap)  # [1, 3, 2, 4, 5, 9, 6]
