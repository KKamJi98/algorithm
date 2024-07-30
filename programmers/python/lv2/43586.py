# https://school.programmers.co.kr/learn/courses/30/lessons/42586 - [기능개발]
from collections import deque


def solution(progresses, speeds):
    result_queue = deque()
    progresses_deque = deque(progresses)
    speeds_deque = deque(speeds)

    while progresses_deque:
        for idx in range(0, len(progresses_deque)):
            progresses_deque[idx] += speeds_deque[idx]

        complete = 0
        for idx in range(0, len(progresses_deque)):
            if progresses_deque[0] >= 100:
                progresses_deque.popleft()
                speeds_deque.popleft()
                complete += 1
        if complete > 0:
            result_queue.append(complete)

    return list(result_queue)


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
