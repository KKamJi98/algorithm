# https://school.programmers.co.kr/learn/courses/30/lessons/12945 - [ 피보나치 수 ]


def solution(n):
    fibonacci: list[int] = [0 for _ in range(n + 1)]
    fibonacci[0] = 0
    fibonacci[1] = 1

    for i in range(2, n + 1):
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]

    return fibonacci[n] % 1234567


print(solution(5))
