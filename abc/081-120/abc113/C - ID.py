n, m = map(int, input().split())
py = [list(map(int, input().split())) + [i] for i in range(m)]
py.sort()

ans = []
for i in range(m):
    p = py[i][0]
    y = py[i][1]
    key = py[i][2]
    if i == 0:
        ans.append([p, 1, key])
    elif i >= 1:
        if ans[i - 1][0] == p:
            ans.append([p, ans[i - 1][1] + 1, key])
        else:
            ans.append([p, 1, key])

ans = sorted(ans, key=lambda x: x[2])
for i in range(m):
    print(format(ans[i][0], '06'), end='')
    print(format(ans[i][1], '06'))
