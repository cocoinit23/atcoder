import fractions
from functools import reduce

n = int(input())
t = [int(input()) for _ in range(n)]

ans = reduce(lambda x, y: x * y // fractions.gcd(x, y), t)
print(ans)
