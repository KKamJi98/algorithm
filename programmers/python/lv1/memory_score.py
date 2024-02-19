# https://school.programmers.co.kr/learn/courses/30/lessons/176963 - [ 추억 점수 ]
def solution(name, yearning, photo):
    answer = list()
    for i in photo:
        score = 0
        for j in range (len(i)):
            try:
                idx = name.index(i[j])
                score += yearning[idx]
            except:
                continue
        answer.append(score)
    return answer


name = ["may", "kein", "kain", "radi"]	
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
solution(name, yearning, photo)