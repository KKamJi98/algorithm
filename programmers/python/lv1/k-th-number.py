# https://school.programmers.co.kr/learn/courses/30/lessons/42748 - [ K번째수 ]

def solution(array, commands):
    answer = []
    for command in commands:
        selectedArray = array[command[0]-1:command[1]]
        selectedArray.sort()
        print(selectedArray)
        answer.append(selectedArray[command[2]-1])
    return answer
    
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))