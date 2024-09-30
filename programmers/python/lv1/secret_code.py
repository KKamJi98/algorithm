# https://school.programmers.co.kr/learn/courses/30/lessons/155652 - [ 둘만의 암호 ]


def solution(s, skip, index):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    answer = ""
    for curAlpha in skip:
        alpha = alpha.replace(curAlpha, "")
    for curAlpha in s:
        idx = alpha.index(curAlpha)
        for i in range(index):
            idx += 1
            if idx >= len(alpha):
                idx = 0
            curAlpha = alpha[idx]
        answer += curAlpha
    return answer


s = "aukks"
skip = "wbqd"
index = 5
print(solution(s, skip, index))
