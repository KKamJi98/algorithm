def solution(wallpaper):
    lux, luy = float("inf"), float("inf")  # 시작점
    rdx, rdy = -float("inf"), -float("inf")  # 끝점

    for x in range(len(wallpaper[0])):
        for y in range(len(wallpaper)):
            if wallpaper[y][x] == "#":
                if x < lux:
                    lux = x
                if x > rdx:
                    rdx = x
                if y < luy:
                    luy = y
                if y > rdy:
                    rdy = y
    answer = [luy, lux, rdy + 1, rdx + 1]
    return answer


wallpaper = [".#...", "..#..", "...#."]
print(solution(wallpaper))
