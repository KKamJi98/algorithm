# https://www.acmicpc.net/problem/10828 - 스택 (Silver 4)
# Stack
import sys

input = sys.stdin.readline

n = int(input())
stack = []
out = []

for _ in range(n):
    command = input().rstrip().split()

    if command[0] == "push":
        stack.append(int(command[1]))
    elif command[0] == "pop":
        out.append(str(stack.pop() if stack else -1))
    elif command[0] == "size":
        out.append(str(len(stack)))
    elif command[0] == "empty":
        out.append("0" if stack else "1")
    elif command[0] == "top":
        out.append(str(stack[-1] if stack else -1))
    else:
        print("Wrong command")

print("\n".join(out))
