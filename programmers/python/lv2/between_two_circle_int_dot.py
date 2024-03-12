# https://school.programmers.co.kr/learn/courses/30/lessons/181187 - 두 원 사이의 정수 쌍
import math

def solution(r1, r2):
    # 작은 것
    count = 0
    for x in range(1, r2+1):
        max_value = math.floor(math.sqrt(math.pow(r2,2) - math.pow(x,2)))
        if x >= r1:
            min_value = 0
        else:
            min_value = math.ceil(math.sqrt(math.pow(r1,2) - math.pow(x,2)))
        count += max_value - min_value + 1
                
    return count * 4
    
r1 = 2
r2 = 3
print(solution(r1, r2))