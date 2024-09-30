# https://school.programmers.co.kr/learn/courses/30/lessons/147355 - [크기가 작은 부분 문자열]
def solution(t, p):
    def sub_string_checker(t_sub) -> bool:
        if int(t_sub) <= int(p):
            return True
        return False

    result = []
    for idx in range(0, len(t) - len(p) + 1):
        tmp = t[idx : idx + len(p)]
        if sub_string_checker(tmp):
            result.append(tmp)

    return len(result)


print(solution("500220839878", "7"))  # result = 2
