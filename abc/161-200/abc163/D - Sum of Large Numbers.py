n, k = map(int, input().split())
mod = 10 ** 9 + 7

cum = [0] * (n + 2)
cum[1] = 1
for i in range(2, n + 2):
    cum[i] = i + cum[i - 1]

ans = 0
for j in range(k, n + 2):
    small = cum[j]
    big = cum[n + 1] - cum[n - j + 1]
    ans += big - small + 1
    ans %= mod

print(ans % mod)
