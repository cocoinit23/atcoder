n, m = map(int, input().split())
ans = 0

if n >= m:
    ans = m // 2
else:
    ans = n + (m - 2 * n) // 4

print(ans)
