# https://leetcode.com/problems/min-cost-climbing-stairs
# DP (bottom-up) O(n)

# 완전 탐색, 재귀를 사용할 경우 10^8 O(2^n) 으로 시간 초과 - 최대 2^1000
from typing import List


class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0] * (len(cost) + 1)
        min_cost[0] = 0
        min_cost[1] = 0

        for i in range(2, len(cost) + 1):
            min_cost[i] = min(
                min_cost[i - 1] + cost[i - 1], min_cost[i - 2] + cost[i - 2]
            )

        return min_cost[-1]

    def top_down(self, cost: List[int], idx) -> int:
        if idx == 0 or idx == 1:
            return 0
        if idx not in self.memo:
            self.memo[idx] = min(
                self.top_down(cost, idx - 1) + cost[idx - 1],
                self.top_down(cost, idx - 2) + cost[idx - 2],
            )
        return self.memo[idx]


s = Solution()
kkam_list = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(s.minCostClimbingStairs(kkam_list))
print(s.top_down(kkam_list, len(kkam_list)))
