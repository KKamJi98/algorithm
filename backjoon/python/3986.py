# https://www.acmicpc.net/problem/3986 - [ 좋은 단어 ]

def solution(myStr: str) -> bool:
    stack = list()
    for i in myStr:
        if len(stack) == 0 or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False
    

N = int(input())

count = 0
for i in range(N):
    myStr = input()
    count += 1 if solution(myStr) else 0
        
print(count)