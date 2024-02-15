# https://school.programmers.co.kr/learn/courses/30/lessons/250121 - [ 데이터 분석 ]

def solution(data, ext, val_ext, sort_by):
    maps = ["code", "date", "maximum", "remain"]
    selector = maps.index(ext)
    sortSelector = maps.index(sort_by)
    tmp = [i for i in data if i[selector] < val_ext]
    tmp.sort(key = lambda x: x[sortSelector])
    return tmp

data = [[1, 20300104, 847, 80], [2, 20300804, 100, 37], [3, 20300401, 10, 8], [4, 20240731, 120, 72], [5, 20390101, 130, 1]]
ext = "code"
val_ext = 3
sort_by = "maximum"
print(solution(data, ext, val_ext, sort_by))