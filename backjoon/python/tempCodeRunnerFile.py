# # https://www.acmicpc.net/problem/2178 - [ 미로 탐색 ]
import sys
from collections import deque

def bfs(row, col):
    deque.append([row, col])
    dist = 0
    mv = [[1,0], [-1,0], [0,-1], [0,1]] # 상하좌우
    while len(deque) != 0:
        curRow, curCol = deque.popleft()
        if array[curRow][curCol] == '1':
            dist += 1
            distance[curRow][curCol] = dist
            array[curRow][curCol] = '0'
            if curRow == n-1 or curCol == m-1:
                return distance[curRow][curCol]
            for next in mv:
                if curRow + next[0] < 0 or curRow + next[0] >= n or curCol + next[1] < 0 or curCol + next[1] >= m:
                    continue
                deque.append([curRow + next[0], curCol + next[1]])
                
    return dist

n, m = map(int, sys.stdin.readline().rstrip().split(' '))

# array = []
# for i in range(n):
#     array.append(sys.stdin.readline().rstrip())
array = [list(input().strip()) for _ in range(n)] # 문자열을 문자의 리스트로 변환
distance = [[0 for j in range(m)] for i in range(n)]
# print(distance)
deque = deque()

print(bfs(0, 0))
# print( deque.pop()[0] )
