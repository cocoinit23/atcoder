n, m = map(int, input().split())
x = list(map(int, input().split()))
cy = [list(map(int, input().split())) for _ in range(m)]

bonus = {c: y for c, y in cy}

dp = [[0] * (n + 1) for _ in range(n)]
dp[0][1] = x[0]
if 1 in bonus:
    dp[0][1] += bonus[1]

for coin in range(1, n):
    for count in range(coin + 2):
        if count == 0:
            dp[coin][0] = max(dp[coin - 1])
        else:
            dp[coin][count] = dp[coin - 1][count - 1] + x[coin]
            if count in bonus:
                dp[coin][count] += bonus[count]

ans = max(dp[n - 1])

print(ans)
