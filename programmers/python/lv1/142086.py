# https://school.programmers.co.kr/learn/courses/30/lessons/142086 - [ 가장 가까운 글자 ]

def solution(s):
    # O(n)

    # s와 똑같은 크기를 갖는 배열 answer 선언 (0 초기화)
    answer = [0 for _ in range(len(s))]
    # dict 선언
    dict = {}
    # 현재 인덱스에 존재하는 문자열이 있는지 확인 (반복)
    #   없으면 answer[cur_idx]에 -1 저장 후 dict에 현재 인덱스 저장
    #   있으면 answer[cur_idx] = cur_idx - dict[s[cur_idx]] 후 dict 갱신
    for cur_idx in range(0, len(answer)):
        if s[cur_idx] not in dict:
            answer[cur_idx] = -1
        else:
            answer[cur_idx] = cur_idx - dict[s[cur_idx]]
        dict[s[cur_idx]] = cur_idx
    print(answer)
    return answer

solution("banana")
