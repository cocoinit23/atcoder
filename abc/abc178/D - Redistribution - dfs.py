from functools import lru_cache
import sys

sys.setrecursionlimit(2000)

s = int(input())
mod = 10 ** 9 + 7


@lru_cache(maxsize=None)
def dfs(n):
    if n <= 2:
        return 0
    elif 3 <= n <= 5:
        return 1
    else:
        count = 1
        for i in range(3, n + 1):
            count += dfs(n - i)
            count %= mod

        return count % mod


ans = dfs(s)
print(ans)
