n = int(input())
mod = 998244353

ans = 0
m = n
while m > 0:
    keta = len(str(m))
    start = 10 ** (keta - 1)
    end = min(n, int('9' * keta))
    x = end - start + 1
    x %= mod
    val = x * (x + 1) // 2
    ans += val % mod
    m //= 10

ans %= mod
print(ans)
