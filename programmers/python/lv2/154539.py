# https://school.programmers.co.kr/learn/courses/30/lessons/154539 - [ 뒤에 있는 큰 수 찾기 ]

# O(n^2) => 시간초과의 지름길
def solution(numbers):
    result = [-1] * len(numbers)  # 결과 배열을 -1로 초기화
    stack = []

    for i in range(len(numbers)):
        # 스택이 비어있지 않고 현재 숫자가 스택의 인덱스에 해당하는 숫자보다 큰 경우
        while stack and numbers[i] > numbers[stack[-1]]:
            idx = stack.pop()  # 스택에서 인덱스를 팝
            result[idx] = numbers[i]  # 해당 인덱스의 결과를 현재 숫자로 설정
        stack.append(i)  # 현재 인덱스를 스택에 추가

    return result

print(solution([9, 1, 5, 3, 6, 2]))

