# https://www.acmicpc.net/problem/5430 - [ AC ]
# 죠깥은 문제 [이거 본사람은 이 문제 풀지 말도록.]

import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for j in range(T):
    commands = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    data = sys.stdin.readline().rstrip()[1:-1]
    arr = deque(data.split(',')) if n > 0 else deque()
    
    error = False
    reverse = False
        
    for command in commands:
        if command == "R":
            reverse = not reverse
        elif command == "D":
            if not arr:
                error = True
                break
            if reverse:
                arr.pop()
            else:
                arr.popleft()
        
    if error:
        print('error')
    else:
        if reverse:
            arr.reverse()
        print("[" + ",".join(arr) + "]")
    