import math
from collections import Counter

n = int(input())
f = math.factorial(n)
mod = 10 ** 9 + 7

factor = []
while f % 2 == 0:
    factor.append(2)
    f //= 2
x = 3
while x ** 2 <= f:
    if f % x == 0:
        factor.append(x)
        f //= x
    else:
        x += 2

if f != 1:
    factor.append(f)

c = Counter(factor)
ans = 1
for i in c.values():
    ans *= (i + 1)
    ans %= mod

print(ans)
