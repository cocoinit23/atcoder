n = int(input())
s = 'abcdefghij'


def dfs(ans, ref):
    if len(ans) == n:
        print(ans)
    else:
        l = [s[i] for i in range(ref + 1)]
        for x in l:
            if x == l[ref]:
                dfs(ans + x, ref + 1)
            else:
                dfs(ans + x, ref)


dfs('', 0)
