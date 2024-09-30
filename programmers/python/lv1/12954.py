# https://school.programmers.co.kr/learn/courses/30/lessons/12954 - [ x만큼 간격이 있는 n개의 숫자 ]


def solution(x, n) -> list[int]:
    if x == 0:
        return [0 for _ in range(n)]
    answer: list[int] = [ele for ele in range(x, x * n + x, x)]
    return answer


print(solution(2, 5))
