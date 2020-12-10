h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]

ans = [[''] * w for _ in range(2 * h)]

for i in range(2 * h):
    for j in range(w):
        ans[i][j] = c[i // 2][j]

for line in ans:
    print(''.join(line))
