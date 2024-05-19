# https://leetcode.com/problems/design-browser-history/description/

# Intuition
# I considered using either a list or a linked list.

# Approach
# Initially, I considered using a list. However, since the visit function requires deleting all previous history, using a list would result in an O(n) time complexity for deletion. 
# Therefore, I opted for a linked list. Given that in browser usage, the visit function is typically used more frequently than back or forward, I decided to use a linked list to solve the problem efficiently.

class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = self.current = Node(val=homepage)
    def visit(self, url: str) -> None:
        new_node = Node(val=url)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = self.current.next
    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.prev is None:
                break
            self.current = self.current.prev
        return self.current.val
    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.next is None:
                break
            self.current = self.current.next
        return self.current.val