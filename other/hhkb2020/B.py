h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                if 0 <= i + x < h and 0 <= j + y < w and s[i + x][j + y] == '.':
                    ans += 1

print(ans // 2)
