# https://school.programmers.co.kr/learn/courses/30/lessons/1844 - 게임 맵 최단거리
from collections import deque

# bfs로 순회
# 1. visit[row][col] 0으로 초기화
# 2. visit[next_row][next_col] = visit[cur_row][cur_col]
# 3. visit[0][0]에서 시작. visit[row][col] 값 리턴
#     3.1 만약 visit[row][col] == 0 이면 -1 리턴


def solution(maps):
    move_row = [1, -1, 0, 0]
    move_col = [0, 0, -1, 1]
    max_row = len(maps)
    max_col = len(maps[0])
    visit = [[0] * max_col for i in range(max_row)]  # 2차원 배열 이게 효율적인가?

    # for i in visit:
    #     print(i)

    q = deque()
    q.append([0, 0])
    visit[0][0] = 1

    while q:
        cur_row, cur_col = q.popleft()

        for i in range(0, 4):
            next_row = cur_row + move_row[i]
            next_col = cur_col + move_col[i]
            if next_row < 0 or next_row >= max_row:
                continue
            if next_col < 0 or next_col >= max_col:
                continue
            if visit[next_row][next_col] != 0 or maps[next_row][next_col] != 1:
                continue
            visit[next_row][next_col] = visit[cur_row][cur_col] + 1
            q.append([next_row, next_col])
    if visit[max_row - 1][max_col - 1] == 0:
        return -1
    else:
        return visit[max_row - 1][max_col - 1]


print(
    solution(
        [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1],
        ]
    )
)
