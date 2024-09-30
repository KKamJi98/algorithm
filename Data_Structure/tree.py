from collections import deque


class Node:
    def __init__(
        self, value: int = 0, left: "Node" = None, right: "Node" = None
    ) -> None:
        self.left = left
        self.right = right
        self.value = value


class BinaryTree:
    def __init__(self):
        self.root = None

    def bfs(self):
        visited = []
        if self.root is None:
            return visited
        q = deque()
        q.append(self.root)
        while q:
            cur_node = q.popleft()
            visited.append(cur_node.value)

            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
        return visited


bt = BinaryTree()
bt.root = Node(5)
bt.root.left = Node(3)
bt.root.left.left = Node(1)
bt.root.left.right = Node(4)
bt.root.right = Node(7)
bt.root.right.left = Node(6)
bt.root.right.right = Node(8)
print(bt.bfs())
