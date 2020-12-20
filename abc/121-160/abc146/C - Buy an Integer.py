def price(n):
    return a * n + b * len(str(n))


a, b, x = map(int, input().split())

r = 10 ** 9 + 1
l = 0

if price(10 ** 9) <= x:
    print(10 ** 9)
else:
    while r - l > 1:
        mid = (r + l) // 2
        if price(mid) <= x:
            l = mid
        else:
            r = mid

    print(l)
