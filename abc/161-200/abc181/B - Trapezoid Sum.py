n = int(input())

ans = 0
for _ in range(n):
    a, b = map(int, input().split())
    samples = b - a + 1
    ans += (a + b) * samples // 2

print(ans)
