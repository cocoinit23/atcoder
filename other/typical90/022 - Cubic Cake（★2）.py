from typing import List
from functools import reduce
import math


def GreatestCommonDivisor(int_list: List[int]) -> int:
    return reduce(math.gcd, int_list)


a, b, c = map(int, input().split())

gcd = GreatestCommonDivisor([a, b, c])

ans = 0
ans += a // gcd - 1
ans += b // gcd - 1
ans += c // gcd - 1
print(ans)
