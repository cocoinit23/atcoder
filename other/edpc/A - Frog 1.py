n = int(input())
h = [int(x) for x in input().split()] + [0] * 10

dp = [10 ** 10] * (n + 10)
dp[0] = 0

for i in range(n):
    cost1 = abs(h[i + 1] - h[i])
    cost2 = abs(h[i + 2] - h[i])
    dp[i + 1] = min(dp[i + 1], dp[i] + cost1)
    dp[i + 2] = min(dp[i + 2], dp[i] + cost2)

print(dp[n - 1])
