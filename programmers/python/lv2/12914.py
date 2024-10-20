# https://school.programmers.co.kr/learn/courses/30/lessons/12914 - [ 멀리 뛰기 ]

def solution(n):
    my_list = [0] * (n + 1)
    if n < 3:
        return n
    my_list[1] = 1
    my_list[2] = 2
    
    for idx in range(3, n + 1):
        my_list[idx] = my_list[idx-1] + my_list[idx-2]

    return my_list[n]%1234567


print(solution(3))
