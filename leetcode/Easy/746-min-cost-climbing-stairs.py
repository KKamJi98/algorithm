# https://leetcode.com/problems/min-cost-climbing-stairs
# DP (bottom-up) O(n)

# 완전 탐색, 재귀를 사용할 경우 10^8 O(2^n) 으로 시간 초과 - 최대 2^1000
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0] * (len(cost) + 1)
        min_cost[0] = 0
        min_cost[1] = 0
        
        for i in range(2, len(cost) + 1):
            min_cost[i] = min(min_cost[i-1] + cost[i-1], min_cost[i-2] + cost[i-2])
            
        return min_cost[-1]
            
s = Solution()
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))