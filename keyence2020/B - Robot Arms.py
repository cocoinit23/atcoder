n = int(input())
xl = [list(map(int, input().split())) for _ in range(n)]

lr = []
for i in range(n):
    l = max(xl[i][0] - xl[i][1], 0)
    r = max(xl[i][0] + xl[i][1], 0)
    lr.append([l, r])

lr.sort(key=lambda x: x[1])
keep = [False] * n

cur = 0
for i in range(n):
    if cur <= lr[i][0]:
        keep[i] = True
        cur = lr[i][1]

ans = sum(keep)
print(ans)
