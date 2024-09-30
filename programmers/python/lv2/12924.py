# https://school.programmers.co.kr/learn/courses/30/lessons/12924 - [ 숫자의 표현 ]


def solution(n):
    answer = 0

    def checker(num) -> bool:
        sum = 0
        for i in range(num, n + 1):
            sum += i
            if sum == n:
                return True
            elif sum > n:
                return False

    for i in range(1, n + 1):
        if checker(i):
            answer += 1

    return answer


print(solution(15))
