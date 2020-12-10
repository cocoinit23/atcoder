from functools import reduce

n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]


def dfs(num, cur):
    if cur == n:
        return reduce(lambda x, y: x ^ y, num) == 0

    result = []
    for i in t[cur]:
        result.append(dfs(num + [i], cur + 1))

    return any(result)


ans = dfs([], 0)
print('Found') if ans else print('Nothing')
