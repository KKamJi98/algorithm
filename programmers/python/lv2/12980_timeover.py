# https://school.programmers.co.kr/learn/courses/30/lessons/12980 - [ 점프와 순간 이동 ]


def solution(n):
    numbers = {}

    def checker(num, count):
        current_num = num
        while current_num <= n:
            if current_num not in numbers:
                numbers[current_num] = count
                current_num *= 2
            else:
                break

    checker(1, 1)

    for i in range(2, n + 1):
        if i not in numbers:
            temp_count = 0
            temp_num = i
            while temp_num > 0:
                if temp_num not in numbers:
                    temp_num -= 1
                else:
                    temp_count = numbers[temp_num] + (i - temp_num)
                    break
            checker(i, temp_count)
    return numbers[n]


print(solution(6))
