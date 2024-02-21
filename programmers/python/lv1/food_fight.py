# https://school.programmers.co.kr/learn/courses/30/lessons/134240 - [ 푸드 파이트 대회 ]

def solution(food):
    answer = str()
    for i in range(1, len(food)):
        quantity = food[i] // 2
        for j in range(quantity):
            answer += str(i)
    return answer+"0"+answer[::-1]

food = [1, 3, 4, 6]	
print(solution(food))