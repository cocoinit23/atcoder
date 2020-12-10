n = int(input())
ng = [int(input()) for _ in range(3)]

dp = [1e9] * (n + 1)
dp[n] = 0
for i in range(n, 0, -1):
    if i in ng:
        continue

    for j in range(1, 4):
        if i - j >= 0:
            dp[i - j] = min(dp[i] + 1, dp[i - j])

print('YES') if dp[0] <= 100 else print('NO')
