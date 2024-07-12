# https://school.programmers.co.kr/learn/courses/30/lessons/154538 - [숫자 변환하기]
from collections import deque


def solution(x, y, n):
    q = deque()
    visited = {}
    q.append(x)
    visited[x] = 0
    while q:
        current = q.popleft()
        if current * 2 <= y:
            if current * 2 in visited:
                continue
            q.append(current * 2)
            visited[current * 2] = visited[current] + 1
        if current * 3 <= y:
            if current * 3 in visited:
                continue
            q.append(current * 3)
            visited[current * 3] = visited[current] + 1
        if current + n <= y:
            if current + n in visited:
                continue
            q.append(current + n)
            visited[current + n] = visited[current] + 1

    if y in visited:
        return visited[y]
    else:
        return -1


print(solution(10, 40, 2))  # 예상 출력: 3
