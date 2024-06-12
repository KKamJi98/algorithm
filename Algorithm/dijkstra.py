import heapq


def dijkstra(graph, start, final):
    costs = {}
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs:
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_v))
    return costs[final]


graph = {
    'A': [(1, 'B'), (2, 'C')],
    'B': [(2, 'D'), (5, 'E')],
    'C': [(1, 'D')],
    'D': [(1, 'E'), (2, 'F')],
    'E': [(1, 'F')],
    'F': []
}
print(dijkstra(graph, 'A', 'F'))  # 5
