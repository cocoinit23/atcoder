n, k = map(int, input().split())


def g1(x):
    x = sorted(list(str(x)), reverse=True)
    x = "".join(x)

    return int(x)


def g2(x):
    x = sorted(list(str(x)))
    x = "".join(x)

    return int(x)


def f(x):
    return g1(x) - g2(x)


ans = n
for i in range(k):
    temp = f(ans)
    if ans == temp:
        break
    else:
        ans = temp

print(ans)
