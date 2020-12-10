n = int(input())
mod = 10007

if n <= 2:
    print(0)
elif n == 3:
    print(1)
else:
    dp = [0] * (n + 1)
    dp[3] = 1

    for i in range(4, n + 1):
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
        dp[i] %= mod

    print(dp[n])
