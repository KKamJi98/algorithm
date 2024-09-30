# https://school.programmers.co.kr/learn/courses/30/lessons/12916 - [ 문자열 내 p와 y의 개수 ]


def solution(s):
    s = s.lower()
    num_of_p = 0
    num_of_y = 0

    for ele in s:
        if ele == "p":
            num_of_p += 1
        elif ele == "y":
            num_of_y += 1

    if num_of_p == 0 and num_of_y == 0:
        return True
    elif num_of_p == num_of_y:
        return True
    else:
        return False


solution("sPoooyY")
