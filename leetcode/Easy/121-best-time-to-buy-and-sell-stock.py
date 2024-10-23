# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


solution_test = Solution()
print(solution_test.maxProfit([1, 2, 4]))  # 출력: 3
print(solution_test.maxProfit([7, 1, 5, 3, 6, 4]))  # 출력: 5
print(solution_test.maxProfit([7, 6, 4, 3, 1]))  # 출력: 0
print(solution_test.maxProfit([2, 4, 1]))  # 출력: 2
