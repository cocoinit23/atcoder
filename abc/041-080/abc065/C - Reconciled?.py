from functools import reduce

n, m = map(int, input().split())
mod = 10 ** 9 + 7

if abs(n - m) >= 2:
    print(0)
elif abs(n - m) == 1:
    a = reduce(lambda x, y: (x * y) % mod, range(1, n + 1))
    b = reduce(lambda x, y: (x * y) % mod, range(1, m + 1))
    ans = (a * b) % mod
    print(ans)
elif n == m:
    c = reduce(lambda x, y: (x * y) % mod, range(1, n + 1))
    ans = (c*c * 2) % mod
    print(ans)
