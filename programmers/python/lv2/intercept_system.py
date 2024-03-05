# https://school.programmers.co.kr/learn/courses/30/lessons/181188 - 요격 시스템

def solution(targets):
    answer = 0
    targets.sort(key = lambda x:[x[1],x[0]])
    
    end = 0
    for target in targets:
        if target[0] >= end:
            answer += 1
            end = target[1]
    
    return answer

targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
print(solution(targets))