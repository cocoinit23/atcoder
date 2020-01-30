import fractions


def func(n, c, d):
    x = n // c
    y = n // d
    z = n // (c * d // fractions.gcd(c, d))

    return n - x - y + z


a, b, c, d = map(int, input().split())

print(func(b, c, d) - func(a - 1, c, d))
