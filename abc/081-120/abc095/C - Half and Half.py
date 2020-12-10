a, b, c, x, y = map(int, input().split())

ans = 0

if a + b >= c * 2:
    ans += min(x, y) * c * 2
    x, y = x - min(x, y), y - min(x, y)
    if [a, b][y > x] >= c * 2:
        ans += max(x, y) * c * 2
    else:
        ans += [a, b][y > x] * max(x, y)
else:
    ans += a * x + b * y

print(ans)
