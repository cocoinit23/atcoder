import math
from functools import reduce

k = int(input())

ans = 0
for a in range(1, k + 1):
    for b in range(1, k + 1):
        for c in range(1, k + 1):
            ans += reduce(math.gcd, [a, b, c])

print(ans)
