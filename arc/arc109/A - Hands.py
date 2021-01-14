a, b, x, y = map(int, input().split())

ans = 0
if a == b:
    ans = x
elif a > b:
    if 2 * x <= y:
        ans = 2 * (a - b) * x - x
    elif x < y:
        ans = (a - b - 1) * y + x
    else:
        ans = (a - b) * y + x
else:
    if 2 * x <= y:
        ans = 2 * (b - a) * x + x
    else:
        ans = (b - a) * y + x

print(ans)
