n, t = map(int, input().split())
tt = list(map(int, input().split()))

ans = 0
for i in range(1, n):
    ans += min(t, tt[i] - tt[i - 1])

print(ans + t)
