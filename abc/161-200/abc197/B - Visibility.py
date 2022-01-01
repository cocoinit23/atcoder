h, w, x, y = map(int, input().split())
masu = [list(input()) for _ in range(h)]

x -= 1
y -= 1

ans = 0
for i in range(x, h):
    curr = masu[i][y]
    if curr == ".":
        ans += 1
    else:
        break

for i in range(x, -1, -1):
    curr = masu[i][y]
    if curr == ".":
        ans += 1
    else:
        break

for i in range(y, w):
    curr = masu[x][i]
    if curr == ".":
        ans += 1
    else:
        break

for i in range(y, -1, -1):
    curr = masu[x][i]
    if curr == ".":
        ans += 1
    else:
        break

ans -= 3
print(ans)
