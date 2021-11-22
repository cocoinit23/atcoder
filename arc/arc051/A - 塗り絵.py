x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())

grid = [[0] * 400 for _ in range(400)]
x1 += 200
x2 += 200
x3 += 200
y1 += 200
y2 += 200
y3 += 200

for i in range(400):
    for j in range(400):
        if r ** 2 >= (x1 - i) ** 2 + (y1 - j) ** 2:
            grid[j][i] += 1

for i in range(x2, x3 + 1):
    for j in range(y2, y3 + 1):
        grid[j][i] += 2

red = False
blue = False
for i in grid:
    for j in i:
        if j == 1:
            red = True
        elif j == 2:
            blue = True

print("YES") if red else print("NO")
print("YES") if blue else print("NO")
