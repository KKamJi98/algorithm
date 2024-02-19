# https://school.programmers.co.kr/learn/courses/30/lessons/178871 - [ 달리기 경주 ]

def solution(players, callings):
    answer = {player: i for i, player in enumerate(players)}
    
    for call in callings:
        idx = answer[call]
        answer[call] -= 1
        answer[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]
    return players



players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
print(solution(players, callings))