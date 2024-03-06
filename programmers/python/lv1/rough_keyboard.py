# https://school.programmers.co.kr/learn/courses/30/lessons/160586 - [ 대충 만든 자판 ]
import sys

def solution(keymap, targets):
    answer = []
    for target in targets:
        totalCount = 0
        found = True
        for element in target:
            minIdx = sys.maxsize
            for curKeyMap in keymap:
                try:
                    curIdx = curKeyMap.index(element)
                    if curIdx < minIdx:
                        minIdx = curIdx
                except ValueError:
                    continue
            if minIdx == sys.maxsize:
                found = False
                break
            totalCount += minIdx + 1
        if not found:
            answer.append(-1)
        else:
            answer.append(totalCount)
    return answer
    
keymap = ["AA"]
targets = ["B"]
print(solution(keymap, targets))