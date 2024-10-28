# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        my_dict = {}
        if not head or head.next is None:
            return False
        current = head

        while current.next:
            if current.next not in my_dict:
                my_dict[current] = 1
                current = current.next
            else:
                return True
        return False
