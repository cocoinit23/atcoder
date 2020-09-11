a, b, c, d, e, f = map(int, input().split())

water = set()
sugar = set()
for i in range(f // (100 * a) + 1):
    for j in range((f - 100 * a * i) // (100 * b) + 1):
        if 100 * a * i + 100 * b * j <= f:
            water.add(100 * a * i + 100 * b * j)

for i in range(f // c + 1):
    for j in range((f - c * i) // d + 1):
        if c * i + d * i <= f:
            sugar.add(c * i + d * j)

ans = (0, 0)
concentration = 0
for w in water:
    if w == 0:
        continue
    for s in sugar:
        if w + s <= f:
            if concentration <= s / (w + s) <= e / (100 + e):
                concentration = s / (w + s)
                ans = (w + s, s)

print(*ans)
