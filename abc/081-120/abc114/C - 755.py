n = int(input())


def dfs(s):
    if int(s) > n:
        return 0

    ans = 1 if sorted(list(set(str(s)))) == ['0', '3', '5', '7'] else 0
    for i in '753':
        ans += dfs(s + i)

    return ans


print(dfs('0'))
