# https://www.acmicpc.net/problem/1926 - [ 그림 ]
# dfs 사용

import sys
sys.setrecursionlimit(10**6)
def dfs(x, y):
    if x < 0 or y < 0 or x >= height or y >= width or array[x][y] == 0:
        return 0
    array[x][y] = 0
    area = 1
    for dx, dy in [(1,0),(-1,0),(0,-1),(0,1)]:
        area += dfs(x+dx, y+dy)
    return area
    

height, width = map(int, sys.stdin.readline().rstrip().split(' '))
array = []
for _ in range(height):
    array.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
    
pictureCount, maxArea = 0, 0

for x in range(height):
    for y in range(width):
        area = dfs(x, y)
        if area > 0:
            pictureCount+=1
        if area > maxArea:
            maxArea = area

print(pictureCount)
print(maxArea)