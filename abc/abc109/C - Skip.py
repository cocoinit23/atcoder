import fractions
from functools import reduce

n, x = map(int, input().split())
xx = [abs(int(i) - x) for i in input().split()]

if n == 1:
    ans = xx[0]
else:
    ans = reduce(fractions.gcd, xx)

print(ans)
