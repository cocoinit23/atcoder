h, w = map(int, input().split())
canvas = [list(input()) for _ in range(h)]

flag = True
for i in range(h):
    for j in range(w):
        now = canvas[i][j]
        if now == '#':
            left = canvas[i][max(0, j - 1)]
            right = canvas[i][min(w - 1, j + 1)]
            up = canvas[max(0, i - 1)][j]
            down = canvas[min(h - 1, i + 1)][j]
            if left == right == up == down == '.':
                flag = False

print('Yes') if flag else print('No')
