# https://school.programmers.co.kr/learn/courses/30/lessons/176962 - [ 과제 진행하기 ]


def solution(plans):
    finished = list()
    stopped = list()

    # plans에 start hour, minute를 모두 분으로 변환, plans[3]을 기준으로 정렬, 첫번째 배열부터 순환
    for i in plans:
        hour = int(i[1][0:2])
        minute = int(i[1][3:5])
        i.append(hour * 60 + minute)
        i[2] = int(i[2])
    plans.sort(key=lambda x: x[3])

    num_of_jobs = len(plans)
    current_job = plans.pop(0)
    current_time = current_job[3]
    while len(finished) != num_of_jobs:
        current_time += 1
        current_job[2] -= 1

        # 현재 진행 중인 과제를 완수하면 finished에 추가
        if current_job[2] == 0:
            finished.append(current_job[0])
            if plans and plans[0][3] == current_time:
                current_job = plans.pop(0)
            elif stopped:
                current_job = stopped.pop()
        elif plans and current_time == plans[0][3]:
            stopped.append(current_job)
            current_job = plans.pop(0)

    return finished


plans = [
    ["aaa", "12:00", "20"],
    ["bbb", "12:10", "30"],
    ["ccc", "12:40", "10"],
]  # [name, start, playtime]
print(solution(plans))
