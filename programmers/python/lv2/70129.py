# https://school.programmers.co.kr/learn/courses/30/lessons/70129 - [이진 변환 반복하기]


def solution(s):
    zero_count = 0
    count = 0
    while len(s) != 1:
        count += 1
        temp_s = []
        for i in s:
            if i == '0':
                zero_count += 1
            else:
                temp_s.append('1')
        next_s = []
        current = len(temp_s)
        while True:
            if current == 1:
                next_s.append('1')
                break
            elif current == 0:
                break
            
            remainder = current % 2
            current = current // 2
            
            if remainder == 1:
                next_s.append('1')
            else:
                next_s.append('0')
        s = next_s
        s.reverse()
            
    return [count, zero_count]

print(solution("110010101001"))