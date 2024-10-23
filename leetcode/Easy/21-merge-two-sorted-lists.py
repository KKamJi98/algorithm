# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional


# ListNode 클래스 정의
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 클래스 정의
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()  # 결과 리스트의 시작점을 위한 더미 노드
        cur = dummy  # 현재 노드를 가리키는 포인터

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1  # list1의 노드를 결과 리스트에 추가
                list1 = list1.next  # list1의 다음 노드로 이동
            else:
                cur.next = list2  # list2의 노드를 결과 리스트에 추가
                list2 = list2.next  # list2의 다음 노드로 이동
            cur = cur.next  # 결과 리스트의 현재 노드 이동

        # 남아 있는 노드를 결과 리스트에 추가
        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2

        return dummy.next  # 더미 노드의 다음 노드를 반환하여 결과 리스트 반환


# 헬퍼 함수: 파이썬 리스트를 연결 리스트로 변환
def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


# 헬퍼 함수: 연결 리스트를 파이썬 리스트로 변환하여 출력
def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)


# 테스트
solution_test = Solution()

# 파이썬 리스트를 연결 리스트로 변환
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

# mergeTwoLists 함수 호출
merged_list = solution_test.mergeTwoLists(list1, list2)

# 결과 출력
print_linked_list(merged_list)  # 출력: [1, 1, 2, 3, 4, 4]
