# https://www.acmicpc.net/problem/1543 - 문서 검색 (Silver 5)
# Brute Force

input_string = input()
input_word = input()

cnt = 0
i = 0

while i <= len(input_string) - len(input_word):
    if input_string[i : i + len(input_word)] == input_word:
        cnt += 1
        i += len(input_word)
    else:
        i += 1

print(cnt)
