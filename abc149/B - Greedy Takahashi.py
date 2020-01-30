a, b, k = map(int, input().split())

if k <= a:
    a = a - k
    print(a, b)
else:
    k = k - a
    a = 0

    if k == 0:
        pass
    elif k >= b:
        b = 0
    else:
        b = b - k

    print(a, b)
