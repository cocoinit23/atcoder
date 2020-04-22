import fractions
from functools import reduce

n = int(input())
a = list(map(int, input().split()))

ans = reduce(fractions.gcd, a)
print(ans)
