# https://leetcode.com/problems/implement-queue-using-stacks/


class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        for _ in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        pop_ele = self.stack2.pop()
        for _ in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return pop_ele

    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        return self.stack1 == []
