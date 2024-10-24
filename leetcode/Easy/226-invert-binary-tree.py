# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        Q = deque()
        Q.append(root)

        while Q:
            current_node = Q.pop()
            current_node.left, current_node.right = (
                current_node.right,
                current_node.left,
            )
            if current_node.left:
                Q.append(current_node.left)
            if current_node.right:
                Q.append(current_node.right)

        return root
