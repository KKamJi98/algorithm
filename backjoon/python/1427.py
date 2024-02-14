# https://www.acmicpc.net/problem/1427 - [ 소트인사이드 ]

import sys

N: str = sys.stdin.readline().rstrip('\n')

# 리스트 생성 후 N에 해당하는 문자 할당
myList = []
for i in range(len(N)):
    myList.append(int(N[i]))
    
myList.sort(reverse=True)

for i in myList:
    print(i, end='')