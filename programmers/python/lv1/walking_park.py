# https://school.programmers.co.kr/learn/courses/30/lessons/172928 - [ 공원 산책 ]


def solution(park, routes):
    hIdx = 0
    wIdx = 0
    for H in range(len(park)):
        for W in range(len(park[H])):
            if park[H][W] == "S":
                hIdx = H
                wIdx = W
                break
    for route in routes:
        checker = True
        tmpH = hIdx
        tmpW = wIdx
        command = route.split(" ")
        command[1] = int(command[1])
        if command[0] == "E":
            for _ in range(command[1]):
                if tmpW + 1 >= len(park[tmpH]):
                    checker = False
                    break
                tmpW += 1
                if park[tmpH][tmpW] == "X":
                    checker = False
                    break
            if checker:
                wIdx = tmpW
        elif command[0] == "W":
            for _ in range(command[1]):
                if tmpW - 1 < 0:
                    checker = False
                    break
                tmpW -= 1
                if park[tmpH][tmpW] == "X":
                    checker = False
                    break
            if checker:
                wIdx = tmpW
        elif command[0] == "N":
            for _ in range(command[1]):
                if tmpH - 1 < 0:
                    checker = False
                    break
                tmpH -= 1
                if park[tmpH][tmpW] == "X":
                    checker = False
                    break
            if checker:
                hIdx = tmpH
        elif command[0] == "S":
            for _ in range(command[1]):
                if tmpH + 1 >= len(park[tmpH]):
                    checker = False
                    break
                tmpH += 1
                if park[tmpH][tmpW] == "X":
                    checker = False
                    break
            if checker:
                hIdx = tmpH
        else:
            print("Wrong Input")
    return hIdx, wIdx


park = ["SOO", "OOO", "OOO"]
routes = ["E 2", "S 2", "W 1"]
print(solution(park, routes))
# solution(park, routes)
# print(len(park[0]))
