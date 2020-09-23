n, k = map(int, input().split())
mod = 998244353
lr = [list(map(int, input().split())) for _ in range(k)]

dp = [0] * (n + 10)
dp[1] = 1
cumsum = [0] * (n + 10)
cumsum[1] = 1

for i in range(2, n + 1):
    for l, r in lr:
        if l >= i:
            continue

        ll = max(1, i - r)
        rr = i - l
        dp[i] += cumsum[rr] - cumsum[ll - 1]
        dp[i] %= mod
    cumsum[i] = cumsum[i - 1] + dp[i]
    cumsum[i] %= mod

print(dp[n] % mod)
