n = int(input())
t = (list(map(int, input().split())))

dp = [[1e9] * (n + 1) for _ in range(10 ** 3 + 1)]
dp[0][0] = 0

for i in range(n + 1):
    for j in range(10 ** 3 + 1):
        if dp[i][j] == 1e9:
            continue

        dp[i + 1][j + t[i]] = min(dp[i][j], dp[i + 1][j + t[i]])

ans=min(dp)
print(ans)
