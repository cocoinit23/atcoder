n = int(input())

ans = 1e9
for _ in range(n):
    a, p, x = map(int, input().split())
    x -= a
    if x > 0:
        ans = min(ans, p)

print(ans) if ans != 1e9 else print(-1)
