n = int(input())
a = [0] + list(map(int, input().split()))

dp = [0] * 101000
dp[1] = 0
dp[2] = abs(a[2] - a[1])
for i in range(3, n + 1):
    cost1 = abs(a[i] - a[i - 1])
    cost2 = abs(a[i] - a[i - 2])
    dp[i] = min(dp[i - 1] + cost1, dp[i - 2] + cost2)

print(dp[n])
