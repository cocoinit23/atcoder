c = [list(input().split(' ')) for _ in range(4)]

ans = [[None] * 4 for i in range(4)]
for i in range(4):
    for j in range(4):
        ans[3-i][3-j] = c[i][j]

for l in ans:
    print(*l)
