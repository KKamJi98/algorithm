# https://www.acmicpc.net/problem/1158 - [ 요세푸스 문제 ]

N, K = map(int, input().split(" "))
peoples = list(range(1, N+1))
idx = K - 1
print("<", end = "")
while len(peoples) != 0:
    print(peoples.pop(idx), end = "")
    if len(peoples) != 0:
        print(", ", end="")
        
    for _ in range(K - 1):
        if idx >= len(peoples):
            idx = 0
        idx += 1
    if idx >= len(peoples):
        idx = 0
print(">")