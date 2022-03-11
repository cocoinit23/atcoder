from collections import Counter

n = int(input())
masu = [list(input()) for _ in range(n)]


def check(arr):
    c = Counter(arr)
    if (c['#'] == 4 and c['.'] == 2) or (c['#'] == 5 and c['.'] == 1) or (c['#'] == 6 and c['.'] == 0):
        print('Yes')
        exit()


limit = n - 5

for i in range(n):
    for j in range(limit):
        yoko = masu[i][j:j + 6]
        check(yoko)

for i in range(n):
    for j in range(limit):
        tate = [x[i] for x in masu[j:j + 6]]
        check(tate)

for i in range(limit):
    for j in range(limit):
        naname = [masu[i + k][j + k] for k in range(6)]
        check(naname)

for i in range(n - 1, n - limit - 1, -1):
    for j in range(limit):
        naname = [masu[i - k][j + k] for k in range(6)]
        check(naname)

print('No')
