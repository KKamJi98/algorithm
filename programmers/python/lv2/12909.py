# https://school.programmers.co.kr/learn/courses/30/lessons/12909 - [ 올바른 괄호 ]

# O(n)
def solution(s):
    stack = []
    
    answer = True
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            elif len(stack) == 0:
                return False
    if len(stack) == 0 :
        return True
    else:    
        return False

result = solution("))")
print(result)