x1, y1, x2, y2 = map(int, input().split())

dist = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

for i, j in dist:
    for k, l in dist:
        if x1 + i + k == x2 and y1 + j + l == y2:
            print('Yes')
            exit()

print('No')
