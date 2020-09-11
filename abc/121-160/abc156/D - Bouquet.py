from functools import reduce

n, a, b = map(int, input().split())
mod = 10 ** 9 + 7


def cmb(r):
    numerator = reduce(lambda x, y: x * y % mod, [n - r + k + 1 for k in range(r)])
    denominator = reduce(lambda x, y: x * y % mod, [k + 1 for k in range(r)])
    return numerator * pow(denominator, mod - 2, mod) % mod


ans = pow(2, n, mod) - 1 - cmb(a) - cmb(b)
print(ans % mod)
