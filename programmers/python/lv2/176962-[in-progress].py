# https://school.programmers.co.kr/learn/courses/30/lessons/176962 - [ 과제 진행하기 ]

from collections import deque

def solution(plans):
    # plans에 start hour, minute를 모두 분으로 변환
    # plans[3]을 기준으로 정렬
    # 첫번째 배열부터 순환 
    for i in plans:
        hour = int(i[1][0:2])
        minute = int(i[1][3:5])
        i.append(hour * 60 + minute)
    plans.sort(key=lambda x: x[3])
        
    print(plans)
    answer = []
    return answer

plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]] # [name, start, playtime]
solution(plans)