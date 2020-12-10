n, m = map(int, input().split())

imos = [0] * (m + 1)
ans = 0
for _ in range(n):
    l, r, s = map(int, input().split())
    l -= 1
    r -= 1
    ans += s
    imos[l] += s
    imos[r + 1] -= s

for i in range(1, m + 1):
    imos[i] += imos[i - 1]

ans -= min(imos[:m])
print(ans)
