# https://www.acmicpc.net/problem/1316 - 그룹 단어 체커 (Silver 5)
# 구현

n = int(input())

input_string_arr = list()

for i in range(n):
    input_string_arr.append(input())

count = 0

for current in input_string_arr:
    current_alphabet_set = set()
    flag = True
    before = ""
    for alpha in current:
        if alpha not in current_alphabet_set:
            current_alphabet_set.add(alpha)
            before = alpha
        elif alpha in current_alphabet_set and before != alpha:
            flag = False
            break
    if flag:
        count += 1

print(count)
