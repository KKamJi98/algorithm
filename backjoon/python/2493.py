# https://www.acmicpc.net/problem/2493 - [ 탑 ]
# 시간 초과 발생 => Stack의 기능 출력하는 것에서만 사용함 Stack을 사용해 O(n^2)에서  O(n)으로 시간 복잡도 개선 가능

import sys

N = int(sys.stdin.readline().rstrip())
kkamList = list(map(int, list(sys.stdin.readline().rstrip().split(" "))))
kkamStack = list(list())
result = [-1] * len(kkamList)

for i in reversed(range(N)):
    if len(kkamStack) == 0:
        kkamStack.append([kkamList[i], i])
        continue
        
    if kkamList[i] >= kkamStack[-1][0]:
        while(len(kkamStack) > 0 and kkamStack[-1][0] <= kkamList[i]):
            value, idx = kkamStack.pop()
            result[idx] = i

    kkamStack.append([kkamList[i], i])
        
for i in result:
    if i == -1:
        print(0, end=' ')
    else:
        print(i+1, end=' ')