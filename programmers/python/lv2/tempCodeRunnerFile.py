# https://school.programmers.co.kr/learn/courses/30/lessons/12946 - [JadenCase 문자열 만들기]

def solution(s):
    result = []
    words = s.split(' ')
    
    for word in words:
        if len(word) == 0:
            result.append('')
        else:
            if word[0].isdigit():
                result.append(word)
            else:
                result.append(word[0].upper() + word[1:].lower())
    # print(result)
    return ' '.join(result)
    
print(solution("for the last week"))  # "For The Last Week"
print(solution("hello  world"))  # "Hello  World"
print(solution("3people unFollowed me"))  # "3people Unfollowed Me"