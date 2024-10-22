# https://school.programmers.co.kr/learn/courses/30/lessons/131701 - [ 연속 부분 수열 합의 개수 ]

def solution(elements):
    n = len(elements)
    double_elements = elements + elements  

    cum_sum = [0] * (2 * n + 1)
    for j in range(2 * n):
        cum_sum[j + 1] = cum_sum[j] + double_elements[j]

    unique_sums = set()

    for i in range(1, n + 1): 
        for j in range(n):
            s = cum_sum[j + i] - cum_sum[j]
            unique_sums.add(s)

    return len(unique_sums)
