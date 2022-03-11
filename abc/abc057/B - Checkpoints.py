n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(m)]

for a, b in ab:
    ans = 10 ** 10
    dist = 10 ** 10
    for i in range(m):
        c, d = cd[i]
        temp = abs(a - c) + abs(b - d)
        if dist > temp:
            dist = temp
            ans = i + 1
    print(ans)
