# https://school.programmers.co.kr/learn/courses/30/lessons/159994 - [ 카드 뭉치 ]
def solution(cards1, cards2, goal):
    for i in goal:
        if cards1 and i == cards1[0]:
            cards1.pop(0)
        elif cards2 and i == cards2[0]:
            cards2.pop(0)
        else:
            return "No"

    return "Yes"


cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
print(solution(cards1, cards2, goal))
