# https://leetcode.com/problems/daily-temperatures/description/

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for cur_day, cur_temp in enumerate(temperatures):
            while stack and stack[-1][1] < cur_temp:
                prev_day, prev_temp = stack.pop()
                ans[prev_day] = cur_day - prev_day
            stack.append([cur_day, cur_temp])
        return ans

S = Solution()
print(S.dailyTemperatures([73,74,75,71,69,72,76,73]))