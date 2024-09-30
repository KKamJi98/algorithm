# https://school.programmers.co.kr/learn/courses/30/lessons/42746 - [가장 큰 수]

# 1. 첫 번째 수가 가장 큰 것 부터 정렬


def solution(numbers):
    str_numbers = [str(number) for number in numbers]
    # 원소의 크기가 0이상 1000 이하이기 때문에 *3
    sorted_numbers = sorted(str_numbers, key=lambda number: number * 3, reverse=True)
    answer = "".join(sorted_numbers)
    # 모든 배열의 요소가 0일 때 0이 리턴되도록, int로 바꾸어주지 않으면 00, 000, 0000 등의 값의 리턴 가능
    return str(int(answer))


solution([0, 0, 0])
