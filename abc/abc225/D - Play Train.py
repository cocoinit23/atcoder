n, q = map(int, input().split())
query = [input() for _ in range(q)]
connect = [[None, None] for _ in range(n + 1)]

for i in query:
    if i[0] == '3':
        flag, x = map(int, i.split())
    else:
        flag, x, y = map(int, i.split())

    if flag == 1:
        connect[x][1] = y
        connect[y][0] = x
    elif flag == 2:
        connect[x][1] = None
        connect[y][0] = None
    elif flag == 3:
        cur = x
        while connect[cur][0] is not None:
            cur = connect[cur][0]

        ans = []
        while True:
            ans.append(cur)
            cur = connect[cur][1]
            if cur is None:
                break

        m = len(ans)
        ans = ' '.join(map(str, ans))
        ans = f'{m} {ans}'
        print(ans)