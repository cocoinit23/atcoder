s = int(input())
mod = 10 ** 9 + 7

dp = [0] * (s + 1)
dp[0] = 1

x = 0
for i in range(3, s + 1):
    x += dp[i - 3]
    dp[i] = x % mod

ans = dp[s] % mod
print(ans)
