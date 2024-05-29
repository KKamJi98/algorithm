# https://leetcode.com/problems/shortest-path-in-binary-matrix/
from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        mv = [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]
        n = len(grid)
        q = deque()
        dist = [[0] * n for i in range(n)]
        q.append((0, 0))
        dist[0][0] = 1
        while q:
            cur_row, cur_col = q.popleft()
            for i in mv:
                next_row = cur_row + i[0]
                next_col = cur_col + i[1]
                if next_row >= 0 and next_row < n and next_col >= 0 and next_col < n and dist[next_row][next_col] == 0 and grid[next_row][next_col] == 0:
                    q.append((next_row, next_col))
                    dist[next_row][next_col] = dist[cur_row][cur_col] + 1
        if dist[n-1][n-1] == 0:
            return -1
        else:
            return dist[n-1][n-1]


s = Solution()
print(s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,1]]))
