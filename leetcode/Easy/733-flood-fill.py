# https://leetcode.com/problems/flood-fill/
from typing import List
from collections import deque


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:

        origin_color = image[sr][sc]
        if origin_color == color:
            return image

        Q = deque()
        Q.append((sr, sc))
        image[sr][sc] = color

        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        while Q:
            cur_row, cur_col = Q.popleft()

            for direction in directions:
                next_row, next_col = cur_row + direction[0], cur_col + direction[1]
                if (
                    0 <= next_row < len(image)
                    and 0 <= next_col < len(image[0])
                    and image[next_row][next_col] == origin_color
                ):
                    Q.append((next_row, next_col))
                    image[next_row][next_col] = color

        # for row in image:
        #     for col in row:
        #         print(col, end=" ")
        #     print()
        return image


test_solution = Solution()
test_solution.floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2)
