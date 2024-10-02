# https://school.programmers.co.kr/learn/courses/30/lessons/42842 - [ 카펫 ]


def solution(brown, yellow):
    def size_checker(input_yellow_row_size, input_yellow_column_size):
        temp_brown = input_yellow_row_size * 2 + input_yellow_column_size * 2 + 4
        if temp_brown == brown:
            return True
        else:
            return False

    def is_integer(num):
        return num % 1 == 0

    for yellow_row_size in range(yellow, 0, -1):
        yellow_column_size = yellow / yellow_row_size
        if not is_integer(yellow_column_size):
            continue

        if size_checker(yellow_row_size, yellow_column_size):
            return [yellow_row_size + 2, int(yellow_column_size + 2)]


print(solution(10, 2))
