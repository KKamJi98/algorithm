# https://school.programmers.co.kr/learn/courses/30/lessons/155651 - [ 호텔 대실 ]


def solution(book_time):
    """
    1. 예약시간이 빠른 순서대로 예약 정렬
    2. 배열 생성 후 맨 처음 예약 배열에 삽입.
        2.1. 배열에 퇴실 시간을 기준으로 + 10분 저장
    3. 다음 예약 검사
        3.1. 만약 현재 배열에 퇴실 시간 + 10분이 입실 시간 보다 작을 시, 해당 값을 현재 예약의 퇴실 시간 +10으로 갱신
        3.2. 만약 현재 배열에 퇴실 시간이 입실시간보다 작은 값이 없을 시, 새로운 배열 할당
    4. 배열의 크기 리턴
    #
    """
    book_time.sort(key=lambda x: int(x[0].replace(":", "")))
    print(book_time)
    book_arr = []
    check_out_hour, check_out_min = map(int, book_time[0][1].split(":"))

    check_out_min += 10
    if check_out_min >= 60:
        check_out_min -= 60
        check_out_hour += 1

    book_arr.append([check_out_hour, check_out_min])

    for book_idx in range(1, len(book_time)):
        flag = False
        check_in_hour, check_in_min = map(int, book_time[book_idx][0].split(":"))
        check_out_hour, check_out_min = map(int, book_time[book_idx][1].split(":"))
        check_out_min += 10

        if check_out_min >= 60:
            check_out_min -= 60
            check_out_hour += 1
        for idx, book in enumerate(book_arr):
            if (
                check_in_hour > book[0]
                or check_in_hour == book[0]
                and check_in_min >= book[1]
            ):
                book_arr[idx] = [check_out_hour, check_out_min]
                flag = True
                break
        if flag == False:
            book_arr.append([check_out_hour, check_out_min])

    print(book_arr)
    return len(book_arr)


print(solution([["09:10", "10:11"], ["10:20", "12:20"]]))
