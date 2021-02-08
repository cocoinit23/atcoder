h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]

ans = 0
for i in range(h - 1):
    for j in range(w - 1):
        cnt = 0
        for dx, dy in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            if grid[i + dy][j + dx] == "#":
                cnt += 1
        if cnt == 1 or cnt == 3:
            ans += 1
print(ans)

