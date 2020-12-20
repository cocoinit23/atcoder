import math
from functools import reduce


def lcm(int_list) -> int:
    return reduce(lambda x, y: (x * y) // math.gcd(x, y), int_list)


n = int(input())
ans = 1 + lcm(range(1, n + 1))

print(ans)
