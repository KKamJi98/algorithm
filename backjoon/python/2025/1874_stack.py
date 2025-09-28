# https://www.acmicpc.net/problem/1874 - 스택 수열 (Silver 2)
# Stack

n = int(input())

stack = []
target = [int(input()) for _ in range(n)]

stack = []
operations = []
next_num = 1

for x in target:
    while next_num <= x:
        stack.append(next_num)
        operations.append("+")
        next_num += 1
    if stack and stack[-1] == x:
        stack.pop()
        operations.append("-")
    else:
        print("NO")
        break
else:
    print("\n".join(operations))
