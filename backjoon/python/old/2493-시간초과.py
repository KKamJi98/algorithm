# https://www.acmicpc.net/problem/2493 - [ 탑 ]
# 시간 초과 발생 => Stack의 기능 출력하는 것에서만 사용함 Stack을 사용해 O(n^2)에서  O(n)으로 시간 복잡도 개선 가능
import sys

N = int(sys.stdin.readline().rstrip())
kkamList = list(map(int, list(sys.stdin.readline().rstrip().split(" "))))
stack = []

for i in reversed(range(N)):
    for j in reversed(range(i)):
        curHeight = kkamList[i]
        if kkamList[j] >= curHeight:
            stack.append(j + 1)
            break
        if j == 0:
            stack.append(0)

stack.append(0)

while len(stack) > 0:
    print(stack.pop(), end=" ")
