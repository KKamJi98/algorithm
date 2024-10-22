# https://school.programmers.co.kr/learn/courses/30/lessons/43162 - [ 네트워크 ]


def solution(n, computers):
    def dfs(computer):
        computers[computer][computer] = 0
        for next in range(n):
            if computers[computer][next] == 1:
                computers[computer][next] = 0
                dfs(next)

    answer = 0
    for i in range(0, len(computers)):
        if computers[i][i] == 1:
            answer += 1
            dfs(i)
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
