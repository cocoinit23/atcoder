h, w = map(int, input().split())

mine = [list(input()) for _ in range(h)]


def update(masu):
    if masu == '.':
        return 1
    elif masu == '#':
        return masu
    else:
        return masu + 1


for i in range(h):
    for j in range(w):
        now = mine[i][j]
        ul = mine[max(i - 1, 0)][max(j - 1, 0)]
        u = mine[max(i - 1, 0)][j]
        ur = mine[max(i - 1, 0)][min(j + 1, w - 1)]
        dl = mine[min(i + 1, h - 1)][max(j - 1, 0)]
        d = mine[min(i + 1, h - 1)][j]
        dr = mine[min(i + 1, h - 1)][min(j + 1, w - 1)]
        r = mine[i][min(j + 1, w - 1)]
        l = mine[i][max(j - 1, 0)]

        if now == '#':
            mine[max(i - 1, 0)][max(j - 1, 0)] = update(ul)
            mine[max(i - 1, 0)][j] = update(u)
            mine[max(i - 1, 0)][min(j + 1, w - 1)] = update(ur)
            mine[min(i + 1, h - 1)][max(j - 1, 0)] = update(dl)
            mine[min(i + 1, h - 1)][j] = update(d)
            mine[min(i + 1, h - 1)][min(j + 1, w - 1)] = update(dr)
            mine[i][min(j + 1, w - 1)] = update(r)
            mine[i][max(j - 1, 0)] = update(l)

for ans in mine:
    print(''.join(list(map(str, ans))).replace('.', '0'))
