# https://school.programmers.co.kr/learn/courses/30/lessons/42587 - [프로세스]
from collections import deque

'''
1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
  3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
'''


def solution(priorities, location):
    q = deque()
    
    for idx in range(0, len(priorities)):
        q.append((idx, priorities[idx]))
        
    print(q)
    pop_count = 0
    while q:
        current = q.popleft()
        if any(current[1] < item[1] for item in q):
            q.append(current)
        else:
            pop_count += 1
            # 실행된 프로세스가 요청된 위치의 프로세스인지 확인
            if current[0] == location:
                return pop_count
        
        
print(solution([2, 1, 3, 2], 2))