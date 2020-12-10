from functools import reduce

w, h = map(int, input().split())
mod = 10 ** 9 + 7

total = reduce(lambda x, y: (x * y) % mod, [i for i in range(1, w + h - 1)])
ww = reduce(lambda x, y: (x * y) % mod, [i for i in range(1, w)])
hh = reduce(lambda x, y: (x * y) % mod, [i for i in range(1, h)])
denominator = (ww * hh) % mod

ans = total * pow(denominator, mod - 2, mod)
print(ans % mod)
