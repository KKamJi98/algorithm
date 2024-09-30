# https://school.programmers.co.kr/learn/courses/30/lessons/178870 - [ 연속된 부분 수열의 합 ]
import sys


def solution(sequence, k):
    answers = []
    sum = 0
    l = 0
    r = -1

    while True:
        if sum < k:
            r += 1
            if r >= len(sequence):
                break
            sum += sequence[r]
        else:
            sum -= sequence[l]
            l += 1
            if l >= len(sequence):
                break

        if sum == k:
            answers.append([l, r])

    answers.sort(key=lambda x: (x[1] - x[0], x[0]))
    return answers[0]


sequence = [1, 1, 1, 2, 3, 4, 5]
k = 5
print(solution(sequence, k))
