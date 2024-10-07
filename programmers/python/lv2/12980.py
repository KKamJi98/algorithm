# https://school.programmers.co.kr/learn/courses/30/lessons/12980 - [ 점프와 순간 이동 ]


def solution(n):
    ans = 0
    while n > 0:
        if n % 2 == 0:
            n = n // 2  # 순간이동 (에너지 소모 없음)
        else:
            n -= 1  # 점프 (에너지 1 소모)
            ans += 1
    return ans
