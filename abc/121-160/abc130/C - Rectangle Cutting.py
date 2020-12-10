w, h, x, y = map(int, input().split())

area = w * h / 2

if x == w / 2 and y == h / 2:
    print(area, 1)
else:
    print(area, 0)
