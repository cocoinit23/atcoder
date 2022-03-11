n, t = map(int, input().split())
ct = [list(map(int, input().split())) for _ in range(n)]

ans = 10 ** 10
for i in range(n):
    cost = ct[i][0]
    time = ct[i][1]
    if time <= t:
        ans = min(ans, cost)

if ans == 10 ** 10:
    ans = 'TLE'

print(ans)
