n = int(input())
a, b, c = map(int, input().split())

dp = [[0] * 3 for _ in range(n)]
dp[0][0] = a
dp[0][1] = b
dp[0][2] = c

for i in range(n - 1):
    i += 1
    a, b, c = map(int, input().split())
    dp[i][0] = max(dp[i - 1][1] + a, dp[i - 1][2] + a)
    dp[i][1] = max(dp[i - 1][0] + b, dp[i - 1][2] + b)
    dp[i][2] = max(dp[i - 1][0] + c, dp[i - 1][1] + c)

ans = max(dp[n - 1])
print(ans)
