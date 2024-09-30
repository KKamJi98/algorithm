# https://school.programmers.co.kr/learn/courses/30/lessons/12939 - [ 최댓값과 최솟값 ]
import math


def solution(s):
    min, max = math.inf, -math.inf

    arr = list(map(int, s.split(" ")))
    print(arr)
    for i in arr:
        if i < min:
            min = i
        if i > max:
            max = i
    return f"{min} {max}"


print(solution("-1 -2 -3 -4"))
