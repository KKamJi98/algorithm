# https://leetcode.com/problems/maximum-depth-of-binary-tree

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        q = deque()
        max_depth = 0
        q.append((root, 1))
        while q:
            cur_node, cur_depth = q.popleft()
            if cur_depth > max_depth:
                max_depth = cur_depth
                
            if cur_node.left:
                q.append((cur_node.left, cur_depth + 1))
            if cur_node.right:
                q.append((cur_node.right, cur_depth + 1))
                
        return max_depth
            
def build_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while i < len(values):
        current = queue.popleft()
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    
    return root

# Example usage
values = [3, 9, 20, None, None, 15, 7]
root = build_tree_from_list(values)
sol = Solution()
print(sol.maxDepth(root))  # Output: 3




