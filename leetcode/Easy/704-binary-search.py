# https://leetcode.com/problems/binary-search/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(start_idx, end_idx):
            if start_idx > end_idx:
                return -1

            root_idx = (start_idx + end_idx) // 2

            if nums[root_idx] == target:
                return root_idx
            elif target < nums[root_idx]:
                return binary_search(start_idx, root_idx - 1)
            else:
                return binary_search(root_idx + 1, end_idx)

        return binary_search(0, len(nums) - 1)


test_solution = Solution()
print(test_solution.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
