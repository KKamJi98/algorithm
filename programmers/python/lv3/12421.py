# https://school.programmers.co.kr/learn/courses/30/lessons/43163 - [ 단어 변환 ]
from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    visited = {word: False for word in words}
    queue = deque()
    queue.append((begin, 0))

    while queue:
        current_word, steps = queue.popleft()
        if current_word == target:
            return steps

        for word in words:
            if not visited[word] and is_one_letter_diff(current_word, word):
                visited[word] = True
                queue.append((word, steps + 1))


def is_one_letter_diff(word1, word2):
    count = 0
    for a, b in zip(word1, word2):
        if a != b:
            count += 1
        if count > 1:
            return False
    return count == 1
