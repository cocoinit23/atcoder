w, h, n = map(int, input().split())
xya = [list(map(int, input().split())) for _ in range(n)]

width = [0, w]
height = [0, h]

for x, y, a in xya:
    if a == 1:
        width = [max(width[0], x), width[1]]
    elif a == 2:
        width = [width[0], min(width[1], x)]
    elif a == 3:
        height = [max(height[0], y), height[1]]
    elif a == 4:
        height = [height[0], min(height[1], y)]

ans = max(0, width[1] - width[0]) * max(0, height[1] - height[0])
print(ans)
