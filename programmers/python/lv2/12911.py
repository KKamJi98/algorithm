# https://school.programmers.co.kr/learn/courses/30/lessons/12911 - [ 다음 큰 숫자 ]


def solution(n) -> int:
    def to_binary(num: int) -> str:
        return bin(num)

    def count_one(binary: str) -> int:
        one_count = 0
        for ele in binary:
            if ele == "1":
                one_count += 1

        return one_count

    binary_n: str = bin(n)[2:]
    count_one_n: int = count_one(binary_n)

    current_number = n
    count_one_next_number = -1
    while count_one_n != count_one_next_number:
        current_number += 1
        current_binary: str = to_binary(num=current_number)[2:]
        count_one_next_number = count_one(current_binary)

    return current_number


print(solution(78))
