# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        print(list1)
        print(list2)
        
test = Solution()
print(test.mergeTwoLists([1,2,4], [1,3,4]))