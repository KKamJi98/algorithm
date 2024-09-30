# https://leetcode.com/problems/unique-paths
# DP


class Solution:
    # bottom-up (for loop)
    def uniquePaths(self, m: int, n: int) -> int:
        board = [[-1] * n for _ in range(m)]

        for i in range(0, n):
            board[0][i] = 1
        for j in range(0, m):
            board[j][0] = 1

        for row in range(1, m):
            for col in range(1, n):
                board[row][col] = board[row - 1][col] + board[row][col - 1]

        return board[m - 1][n - 1]
        # for i in board:
        #     print(i)

    # top-down (recursion)
    def top_down(self, m: int, n: int) -> int:
        board = [[-1] * n for _ in range(m)]

        def dfs(row, col):
            if row == 0 and col == 0:
                board[row][col] = 1
                return board[row][col]
            unique_paths = 0
            if board[row][col] == -1:
                if row >= 1:
                    unique_paths += dfs(row - 1, col)
                if col >= 1:
                    unique_paths += dfs(row, col - 1)
                board[row][col] = unique_paths
            return board[row][col]

        result = dfs(m - 1, n - 1)
        # for i in board:
        #     print(i)
        return result


s = Solution()
print(s.uniquePaths(3, 7))
print(s.top_down(3, 7))
