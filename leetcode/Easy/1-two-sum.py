# https://leetcode.com/problems/two-sum

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}
        for idx, num in enumerate(nums):
            if target - num in new_dict and idx != new_dict[target - num]:
                return [new_dict[target - num], idx]
            new_dict[num] = idx


S = Solution()
print(S.twoSum([3,3], 6))
