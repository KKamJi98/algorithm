# https://school.programmers.co.kr/learn/courses/30/lessons/154538 - [숫자 변환하기]
from collections import deque

# 
def solution(x, y, n):
    if x == y: # 예외처리
        return 0
    
    q = deque()
    visited = {}
    q.append(x)
    visited[x] = 0
    while q:
        current = q.popleft()
        for next_value in [current * 2, current * 3, current + n]:
            if next_value > y or next_value in visited:
                continue
            
            q.append(next_value)
            visited[next_value] = visited[current] + 1
            
            if next_value == y:
                return visited[next_value]

    if y not in visited:
        return -1


print(solution(5, 5, 4))  # 예상 출력: 3
