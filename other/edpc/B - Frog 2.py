n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [0] * n

for i in range(1, n):
    start = max(0, i - k)
    dp[i] = min([cost + abs(h[i] - hh) for cost, hh in zip(dp[start:i], h[start:i])])

print(dp[n - 1])
