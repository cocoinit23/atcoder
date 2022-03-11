t = int(input())


def func(x):
    return x ** 2 + 2 * x + 3


ans = func(func(func(t) + t) + func(func(t)))
print(ans)
