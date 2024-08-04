# https://school.programmers.co.kr/learn/courses/30/lessons/43165 - [ 타겟 넘버 ]

from collections import deque


def solution(numbers, target):
    '''
    1. 첫 번째 인덱스부터 시작 +, - 큐에 추가
    2. 오른쪽 인덱스 +, - 큐에 추가 --- bfs
    '''

    q = deque()
    result = 0

    q.append([0, 0 - numbers[0]])
    q.append([0, 0 + numbers[0]])

    while q:
        cur_idx, cur_value = q.popleft()
        if cur_idx >= len(numbers) - 1:
            if cur_value == target:
                result += 1
        else:
            next_idx = cur_idx + 1
            q.append([next_idx, cur_value + numbers[next_idx]])
            q.append([next_idx, cur_value - numbers[next_idx]])

    # print(f"result = {result}")
    return result


solution([1, 1, 1, 1, 1], 3)
