n = int(input())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

cumsum = [0] * n
cumsum[0] = a[0]
for i in range(1, n):
    cumsum[i] = cumsum[i - 1] + a[i]

ans = 0
for i in range(n):
    ans += a[i] * (cumsum[-1] - cumsum[i]) % mod

print(ans % mod)
