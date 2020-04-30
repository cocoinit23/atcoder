n, m = map(int, input().split())
a = []
for i in range(m):
    a.append(int(input()))

dp = [1] * (n + 10)
for i in range(len(a)):
    dp[a[i]] = 0

for i in range(n + 1):
    if i == 0 or i == 1:
        dp[i] = dp[i] * 1
    else:
        dp[i] = dp[i] * (dp[i - 2] + dp[i - 1])

print(dp[n] % 1000000007)
