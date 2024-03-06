import sys

def solution(keymap, targets):
    answer = []
    for target in targets:
        totalCount = 0
        found = True  # 각 target 문자열에 대해 적어도 하나의 문자가 keymap에 존재하는지 여부를 추적합니다.
        for element in target:
            minIdx = sys.maxsize
            for curKeyMap in keymap:
                try:
                    curIdx = curKeyMap.index(element)
                    if curIdx < minIdx:
                        minIdx = curIdx
                except ValueError:
                    continue
            if minIdx == sys.maxsize:  # 현재 문자가 keymap 어디에도 존재하지 않는 경우
                found = False
                break  # 더 이상 해당 target에 대해 계산하지 않고 루프를 종료합니다.
            totalCount += minIdx + 1
        if not found:  # target의 어떤 문자도 keymap에서 찾을 수 없는 경우
            answer.append(-1)
        else:
            answer.append(totalCount)
    return answer
    
keymap = ["AA"]
targets = ["B"]
print(solution(keymap, targets))