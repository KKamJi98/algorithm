# https://school.programmers.co.kr/learn/courses/30/lessons/12946 - [하노이의 탑]

def hanoi(n, start, end, via):
    if n == 1:
        # print(f"Move disk 1 from {start} to {end}")
        return [[start, end]]
    
    moves = []
    # Step 1: Move n-1 disks from start to via
    moves += hanoi(n-1, start, via, end)
    
    # Step 2: Move the nth disk from start to end
    moves.append([start, end])
    print(f"Move disk {n} from {start} to {end}")
    
    # Step 3: Move the n-1 disks from via to end
    moves += hanoi(n-1, via, end, start)
    
    return moves

def solution(n):
    return hanoi(n, 1, 3, 2)

n = 3  # 원판의 개수
moves = solution(n)
print(moves)