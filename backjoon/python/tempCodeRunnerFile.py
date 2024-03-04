# https://www.acmicpc.net/problem/5430 - [ AC ]

import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for j in range(T):
    commands = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    arr = deque((sys.stdin.readline().strip())[1:-1].split(','))
    error = False
    boolChecker = False    
    for i in range (len(commands)):
        if i < len(commands) -2 and commands[i] == 'R' and commands[i+1] == 'R':
            boolChecker = True
            continue
        if boolChecker == True:
            boolChecker = False
            continue
        if commands[i] == 'R':
            arr.reverse()
        if commands[i] == 'D':
            if len(arr) == 0 or arr[0] == '':
                error = True
                break
            else:
                arr.popleft()
    if error:
        print('error')
    elif len(arr) == 0:
        print("[]")
    else:
        print(f"[{','.join(arr)}]")
    