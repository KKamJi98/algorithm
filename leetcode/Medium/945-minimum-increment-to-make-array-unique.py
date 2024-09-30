# https://leetcode.com/problems/minimum-increment-to-make-array-unique
from typing import List


class Solution:
    # 시간 초과 O(n^2)
    def solution_ver1(self, nums: List[int]) -> int:
        nums_dict = {}
        new_nums = []
        count = 0
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = True
            else:
                new_nums.append(num)

        while new_nums:
            tmp_list = []
            for i in range(0, len(new_nums)):
                count += 1
                new_nums[i] += 1
                if new_nums[i] not in nums_dict:
                    nums_dict[new_nums[i]] = True
                    tmp_list.append(new_nums[i])
            for i in tmp_list:
                new_nums.remove(i)

        return count

    # greedy O(nlogn)
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] - nums[i] + 1
                nums[i] += increment
                count += increment
        print(nums)
        return count


s = Solution()
result = s.minIncrementForUnique([3, 2, 1, 1, 2, 7])
print(result)
