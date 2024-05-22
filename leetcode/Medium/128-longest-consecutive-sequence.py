# https://leetcode.com/problems/longest-consecutive-sequence/ - [sort version]

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        max_count = 0
        cur_count = 1
        prev = nums[0]
        for cur_num in nums:
            if cur_num == prev:
                continue
            if cur_num == prev + 1:
                cur_count += 1
                max_count = max(max_count, cur_count)
            else:
                max_count = max(max_count, cur_count)
                cur_count = 1
            prev = cur_num
        return max(max_count, cur_count)
    
S = Solution()
print(S.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))