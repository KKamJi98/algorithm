# https://school.programmers.co.kr/learn/courses/30/lessons/12981 - [ 영어 끝말잇기 ]


def solution(n, words):
    answer = [0, 0]

    used_words = {}
    used_words[words[0]] = 0
    for i in range(1, len(words)):
        if words[i][0] != words[i - 1][-1] or words[i] in used_words:
            answer = [i % n + 1, i // n + 1]
            break
        used_words[words[i]] = 0

    return answer


print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
