import math
import time

start = time.perf_counter()
# x, y = map(int, input().split())
x, y = 999999, 999999
mod = 10 ** 9 + 7

fac, inv, finv = [], [], []

fac[0] = fac[1] = 1
finv[0] = finv[1] = 1

for i in range(2, 10 * 6):
    fac[i] = fac[i - 1] * i % mod
    finv = finv[i - 1] / i % mod

if (x + y) % 3 != 0:
    print(0)
else:
    n = (x + y) / 3
    a = y - n
    b = x - n

    # res = math.factorial(n) // (math.factorial(a) * math.factorial(b))
    # print(res % mod)

    res = 0

    print(time.perf_counter() - start)
