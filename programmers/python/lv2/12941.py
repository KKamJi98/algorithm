# https://school.programmers.co.kr/learn/courses/30/lessons/12941 - [최솟값 만들기]

def solution(A, B):
    answer = 0
    
    A.sort()
    B.sort(reverse=True)
    
    for i in range(0, len(A)):
        answer += A[i] * B[i]
    
    return answer
    
result = solution([1,4,2], [4,5,4])
print(result)