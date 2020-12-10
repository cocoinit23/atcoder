r, c, k = map(int, input().split())
grid = [list(input()) for _ in range(r)]
imos = [[0] * (c + 1) for _ in range(r)]

for x in range(c):
    for y in range(r):
        if grid[y][x] == 'x':
            for i in range(k):
                if y - i >= 0:
                    imos[y - i][max(0, x - k + 1 + i)] += 1
                    imos[y - i][min(c, x + k - i)] -= 1
                if y + i < r:
                    imos[y + i][max(0, x - k + 1 + i)] += 1
                    imos[y + i][min(c, x + k - i)] -= 1

for x in range(1, c + 1):
    for y in range(r):
        imos[y][x] += imos[y][x - 1]

ans = 0
for x in range(k - 1, c - k + 1):
    for y in range(k - 1, r - k + 1):
        if imos[y][x] == 0:
            ans += 1

print(ans)
