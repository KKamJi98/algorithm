# https://school.programmers.co.kr/learn/courses/30/lessons/161989 - [ 덧칠하기 ]
def solution(n, m, section):
    wall = [0] * (n + 1)
    for i in section:
        wall[i] = 1
    result = 0
    for i in section:
        if wall[i] == 1:
            for j in range(m):
                if i + j <= n:
                    wall[i + j] = 0
            result += 1
    return result


n, m = 4, 1
section = [1, 2, 3, 4]
print(solution(n, m, section))
