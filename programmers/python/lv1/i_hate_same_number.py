# https://school.programmers.co.kr/learn/courses/30/lessons/12906 - [ 같은 숫자는 싫어 ]


def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            answer.append(arr[i + 1])
    return answer


arr = [1, 1, 3, 3, 0, 1, 1]
print(solution(arr))
