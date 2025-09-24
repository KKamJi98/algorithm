# https://www.acmicpc.net/problem/1920 - 수 찾기 (Silver 4)
# set을 사용해 중복 제거

n = int(input())
arr_n = set(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))

out = []
for x in arr_m:
    out.append("1" if x in arr_n else '0')
    
print('\n'.join(out))