# https://school.programmers.co.kr/learn/courses/30/lessons/150370 - [ 개인정보 수집 유효기간 ]


def solution(today, terms, privacies):
    # terms dictionary로 변환
    terms_dict = {}
    result = []

    for i in terms:
        terms_dict[i[0]] = int(i[2:])
        # print(terms_dict) {'A': '6', 'B': '12', 'C': '3'}

    # 파기해야할 개인정보 찾기
    for idx in range(0, len(privacies)):
        current = privacies[idx]
        tmp = list(map(int, [current[0:4], current[5:7], current[8:10]]))
        maintenance_year = tmp[0]
        maintenance_month = tmp[1]
        maintenance_day = tmp[2]
        # print(tmp) [2021, 5, 2]
        # 만기일 찾기
        maintenance_period = terms_dict[current[-1]]
        # print(maintenance_period)
        if maintenance_period >= 12:
            maintenance_year += maintenance_period // 12
            maintenance_period = maintenance_period % 12

        maintenance_month = tmp[1]
        while maintenance_period > 0:
            maintenance_period -= 1
            maintenance_month += 1
            if maintenance_month >= 13:
                maintenance_year += 1
                maintenance_month = 1
        print(maintenance_year, maintenance_month, maintenance_day)  # 2021 11 2
        today_year, today_month, today_day = map(int, today.split("."))  # 2022 5 19
        if today_year > maintenance_year:
            result.append(idx + 1)
        elif today_year == maintenance_year:
            if today_month > maintenance_month:
                result.append(idx + 1)
            elif today_month == maintenance_month and today_day >= maintenance_day:
                result.append(idx + 1)

        # print(maintenance_year, maintenance_month, maintenance_day) # "2021.05.02 A" -> 2021 11 2
    print(result)
    return result


solution(
    "2020.01.01",
    ["Z 3", "D 5"],
    ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"],
)  # result = [1, 3]
