# https://school.programmers.co.kr/learn/courses/30/lessons/250125 - [이웃한 칸]
def solution(board, h, w):
    n: int = len(board)
    count: int = 0
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]
    for i in range(0, 4):
        check_w, check_h = w, h
        if check_w + dw[i] < 0 or check_h + dh[i] < 0 or check_w + dw[i] > n-1 or check_h + dh[i] > n-1:
            continue 
        if board[h][w] == board[check_h+dh[i]][check_w+dw[i]]:
            count += 1
    return count

boardIn = [["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]]
hIn = 0
wIn = 1

print(solution(boardIn, hIn, wIn))