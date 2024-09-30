# https://leetcode.com/problems/climbing-stairs/

# 한번에 하나의 계단 또는 두 개의 계단을 오를 수 있다.
# n개의 계단을 올라가는 방법은 총 몇개가 있는지 리턴해라.

# 1 1
# 2 1+1, 2
# 3 1+1+1, 1+2, 2+1
# 5 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2
# 8 1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 1+2+2, 2+1+2, 2+2+1

result = {1: 1, 2: 2, 3: 3, 4: 5}


class Solution:
    def climb_stairs_brute_force(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        return self.climb_stairs_brute_force(n - 1) + self.climb_stairs_brute_force(
            n - 2
        )

    def climb_stairs_bottom_up(self, n: int) -> int:
        dp = [0] * (n + 2)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climb_stairs_top_down(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n not in result:
            result[n] = self.climb_stairs_top_down(n - 1) + self.climb_stairs_top_down(
                n - 2
            )
        return result[n]


s = Solution()
print(s.climb_stairs_bottom_up(38))
