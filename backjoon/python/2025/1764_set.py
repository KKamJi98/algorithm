# https://www.acmicpc.net/problem/1764
# Set

n, m = list(map(int, input().split()))

not_heard = set(input().rstrip() for _ in range(n))
not_seen = set(input().rstrip() for _ in range(m))

result = sorted(not_heard & not_seen)
print(len(result))
print("\n".join(result))