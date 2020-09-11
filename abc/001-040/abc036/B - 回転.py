n = int(input())
s = [list(input()) for _ in range(n)]

ans = [[''] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        ans[j][n - 1 - i] = s[i][j]

for l in ans:
    print(''.join(l))
