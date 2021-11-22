import math


def num_combinations(x, y):
    return math.factorial(x + y) // math.factorial(x) // math.factorial(y)


a, b, k = map(int, input().split())

n = a + b

ans = ""
for i in range(n):
    if a > 0:
        if b < 0:
            ans += "a" * a
            break
        elif k <= num_combinations(a - 1, b):
            ans += "a"
            a -= 1
        else:
            ans += "b"
            k -= num_combinations(a - 1, b)
            b -= 1
    else:
        ans += "b"
        b -= 1

print(ans)
