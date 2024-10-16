# https://school.programmers.co.kr/learn/courses/30/lessons/12953 - [ N개의 최소공배수 ]

import math


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def solution(arr):
    answer = 1

    for i in arr:
        answer = lcm(answer, i)

    return answer
