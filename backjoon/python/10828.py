# https://www.acmicpc.net/problem/10828 - [ 스택 ]

import sys


def push(stack, int):
    stack.append(int)


def size(stack) -> int:
    return len(stack)


def empty(stack) -> int:
    if len(stack) == 0:
        return 1
    else:
        return 0


def top(stack) -> int:
    if empty(stack) == 0:
        return stack[len(stack) - 1]
    else:
        return -1


def pop(stack) -> int:
    if empty(stack) == 1:
        print(-1)
    else:
        print(stack.pop())


def solution(N):
    stack = []
    for i in range(N):
        command = sys.stdin.readline().rstrip().split(" ")
        # print(command)
        if command[0] == "push":
            push(stack, int(command[1]))
        elif command[0] == "pop":
            pop(stack)
        elif command[0] == "size":
            print(size(stack))
        elif command[0] == "empty":
            print(empty(stack))
        elif command[0] == "top":
            print(top(stack))
        else:
            print("error")


N = int(sys.stdin.readline())
solution(N)
