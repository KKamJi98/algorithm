# https://school.programmers.co.kr/learn/courses/30/lessons/12973 - [ 짝지어 제거하기 ]


def solution(s):
    stack = []

    for ele in s:
        if not stack:
            stack.append(ele)
            continue

        if stack[-1] == ele:
            stack.pop()
        else:
            stack.append(ele)

    if stack:
        return 0
    else:
        return 1


print(solution("aabbccdddd"))
