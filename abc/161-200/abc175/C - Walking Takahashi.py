x, k, d = map(int, input().split())

if x < 0:
    if k <= abs(x) // d:
        ans = abs(x + d * k)
    else:
        k -= abs(x) // d
        x += d * (abs(x) // d)
        if k % 2 == 0:
            ans = abs(x)
        else:
            if x >= 0:
                ans = abs(x - d)
            else:
                ans = abs(x + d)
elif x > 0:
    if k <= x // d:
        ans = abs(x - d * k)
    else:
        k -= x // d
        x -= d * (x // d)
        if k % 2 == 0:
            ans = abs(x)
        else:
            if x >= 0:
                ans = abs(x - d)
            else:
                ans = abs(x + d)
elif x == 0:
    ans = d

print(ans)
