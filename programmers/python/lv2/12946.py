# https://school.programmers.co.kr/learn/courses/30/lessons/12946 - [하노이의 탑]

# O(2^n)
# def solution(n):
#     answer = []
#     def hanoi(n, start, end, via):
#         if n == 1:
#             answer.append([start, end])
#             print(f"move {start} to {end}")
#             return
        
#         hanoi(n-1, start, via, end)
#         print(f"move {start} to {end}")
#         answer.append([start, end])
#         hanoi(n-1, via, end, start)
            
#     hanoi(n, 1, 3, 2)
#     return answer
    
# print(solution(25))

def solution(n):
    answer = []
    def hanoi(n, start, end, via):
        if n == 1:
            answer.append([start, end])
            return
        
        hanoi(n-1, start, via, end)
        answer.append([start, end])
        hanoi(n-1, via, end, start)
            
    hanoi(n, 1, 3, 2)
    return answer

import time

start_time = time.time()
print(solution(25))
end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")
