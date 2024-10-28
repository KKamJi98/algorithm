# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        def binary_search(cur_node):
            if p.val <= cur_node.val <= q.val:
                return cur_node
            elif q.val < cur_node.val:
                if cur_node.left:
                    return binary_search(cur_node.left)
            elif p.val > cur_node.val:
                if cur_node.right:
                    return binary_search(cur_node.right)

        # p가 q보다 항상 작거나 같도록
        if p.val > q.val:
            p, q = q, p
        return binary_search(root)
