l, x, y, s, d = map(int, input().split())

if s == d:
    ans = 0
elif s < d:
    if y - x > 0:
        ans = min((d - s) / (x + y),
                  (l - d + s) / (y - x))
    else:
        ans = (d - s) / (x + y)
else:
    if y - x > 0:
        ans = min((s - d) / (y - x),
                  (l - s + d) / (x + y))
    else:
        ans = (l - s + d) / (x + y)
print(ans)
