# https://www.acmicpc.net/problem/10866 - [ 덱 ]

class Deque:
    def __init__(self):
        self.deque = [0] * 10001
        self.front = 0
        self.rear = 0
    
    def pushFront(self, value):
        if self.front - 1 < 0:
            self.front = 10000
        else:
            self.front -= 1
        self.deque[self.front] = value
            
    def pushBack(self, value):
        self.deque[self.rear] = value
        if self.rear + 1 > 10000:
            self.rear = 0
        else:
            self.rear += 1
        
    def popFront(self):
        if self.empty() == True:
            return -1
        returnValue = self.deque[self.front]
        if self.front == 10000:
            self.front = 0
        else:
            self.front +=1
        return returnValue
    
    def popBack(self):
        if self.empty() == True:
            return -1
        if self.rear == 0:
            self.rear = 10000
        else:
            self.rear -= 1
        return self.deque[self.rear]
    
    def printFront(self):
        print(self.deque[self.front])
        
    def printBack(self):
        print(self.deque[self.rear-1])
        
    def size(self):
        result = 0
        if self.front > self.rear:
            result += self.rear
            result += 10000-self.front+1
        else:
            result = self.rear - self.front
        return result
    
    def empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

import sys
deque = Deque()
N = int(sys.stdin.readline().rstrip())

for i in range(N):
    command = sys.stdin.readline().rstrip().split(" ")
    if command[0] == "push_front":
        deque.pushFront(int(command[1]))
    elif command[0] == "push_back":
        deque.pushBack(int(command[1]))
    elif command[0] == "pop_front":
        print(deque.popFront())
    elif command[0] == "pop_back":
        print(deque.popBack())
    elif command[0] == "size":
        print(deque.size())
    elif command[0] == "empty":
        print(int(deque.empty()))
    elif command[0] == "front":
        if deque.empty() == True:
            print(-1)
        else:
            deque.printFront()
    elif command[0] == "back":
        if deque.empty() == True:
            print(-1)
        else:
            deque.printBack()