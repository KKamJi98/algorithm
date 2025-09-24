# https://www.acmicpc.net/problem/18258 - [ 큐 2 ]
import sys


class KKamQueue:
    def __init__(self):
        self.queue = [0] * 2000001
        self.start: int = 0
        self.end: int = 0

    def push(self, num: int):
        self.queue[self.end] = num
        self.end += 1

    def pop(self) -> int:
        if self.start == self.end:
            return -1
        else:
            self.start += 1
            return self.queue[self.start - 1]

    def size(self) -> int:
        return self.end - self.start

    def empty(self) -> bool:
        if self.end - self.start == 0:
            return True
        else:
            return False

    def front(self) -> int:
        if self.empty():
            return -1
        else:
            return self.queue[self.start]

    def back(self) -> int:
        if self.empty():
            return -1
        else:
            return self.queue[self.end - 1]


def solution(queueIn):
    N = int(sys.stdin.readline())

    for i in range(N):
        command = sys.stdin.readline().rstrip().split(" ")
        if command[0] == "push":
            # print(int(command[1]))
            queueIn.push(int(command[1]))
        elif command[0] == "pop":
            print(queueIn.pop())
        elif command[0] == "size":
            print(queueIn.size())
        elif command[0] == "empty":
            print(int(queueIn.empty()))
        elif command[0] == "front":
            print(queueIn.front())
        elif command[0] == "back":
            print(queueIn.back())


myQueue = KKamQueue()
solution(myQueue)
