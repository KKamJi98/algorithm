# https://leetcode.com/problems/climbing-stairs/

# 한번에 하나의 계단 또는 두 개의 계단을 오를 수 있다.
# n개의 계단을 올라가는 방법은 총 몇개가 있는지 리턴해라.

# 1 1
# 2 1+1, 2
# 3 1+1+1, 1+2, 2+1
# 5 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2
# 8 1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 1+2+2, 2+1+2, 2+2+1

class Solution:
    def __init__(self) -> None:
        self.result = {1: 1, 2: 2, 3: 3, 4: 5}

    def climbStairs(self, n: int) -> int:
        if n in self.result:
            return self.result[n]
        else:
            self.result[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        return self.result[n]

    def climbStairs2(self, n: int) -> int:
        dp = [0] * (n + 2)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


s = Solution()
print(s.climbStairs2(38))
