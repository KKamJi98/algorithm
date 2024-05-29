# https://leetcode.com/problems/number-of-islands - 209

from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        mv = [-1, 0], [1, 0], [0, -1], [0, 1]
        num_of_islands = 0
        q = deque()
        rows, cols = len(grid), len(grid[0])
        visited = [[0 for i in range(cols)] for _ in range(rows)]
        
        for r in range (rows):
            for c in range (cols):
                if grid[r][c] == "1" and visited[r][c] == 0:
                    visited[r][c] = 1
                    q.append((r, c))
                    num_of_islands += 1
                    while q:
                        cur_row, cur_col = q.popleft()
                        for next in mv:
                            next_row = cur_row + next[0]
                            next_col = cur_col + next[1]
                            if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or visited[next_row][next_col] == 1 or grid[next_row][next_col] != "1":
                                continue
                            visited[next_row][next_col] = 1
                            q.append((next_row, next_col))
        return num_of_islands
        
        
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
s = Solution()
print(s.numIslands(grid))