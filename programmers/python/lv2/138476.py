# https://school.programmers.co.kr/learn/courses/30/lessons/138476 - [ 귤 고르기 ]

def solution(k, tangerine):
    # 배열 정렬
    # k 개 고르기 => 종류 확인
    dict = {}
    for i in tangerine:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1

    sorted_tangerine = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    
    count = 0
    answer = 0
    
    for nums in sorted_tangerine:
        count += nums[1]
        answer += 1
        
        if count >= k:
            break
        
    return answer


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
