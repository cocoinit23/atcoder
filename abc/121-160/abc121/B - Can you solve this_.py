n, m, c = map(int, input().split())
b = [int(x) for x in input().split()]

a = []
for i in range(n):
    a.append([int(x) for x in input().split()])

ans = 0
for i in range(n):
    solve = c
    for j in range(m):
        solve += a[i][j] * b[j]
    if solve > 0:
        ans += 1

print(ans)
