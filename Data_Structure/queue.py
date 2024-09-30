import queue

Q = queue.Queue()

#! FIFO Queue
fifo_q = queue.Queue()

# 항목 추가
fifo_q.put(1)
fifo_q.put(2)
fifo_q.put(3)

# 항목 제거
item1 = fifo_q.get()  # 1
item2 = fifo_q.get()  # 2

# 큐의 크기 확인
size = fifo_q.qsize()  # 현재 큐에 있는 항목의 개수

# 큐가 비어 있는지 확인
is_empty = fifo_q.empty()  # 큐가 비어 있으면 True, 아니면 False

# 큐가 가득 찼는지 확인
is_full = fifo_q.full()  # 큐가 가득 찼으면 True, 아니면 False

#! LIFO Queue
lifo_q = queue.LifoQueue()

#! Priority Queue
priority_q = queue.PriorityQueue()

# 우선순위 큐에 항목 추가
priority_q.put((2, "low priority"))
priority_q.put((1, "high priority"))
priority_q.put((3, "lowest priority"))

# 우선순위 큐에서 항목 제거
item1 = priority_q.get()  # (1, "high priority")
item2 = priority_q.get()  # (2, "low priority")
