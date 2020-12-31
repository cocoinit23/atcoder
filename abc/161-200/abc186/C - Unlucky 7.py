n = int(input())


def check10(x: int):
    for s in str(x):
        if s == '7':
            return False
    return True


def check8(x: int):
    base8 = ''
    while x > 0:
        base8 = str(x % 8) + base8
        x //= 8

    for s in base8:
        if s == '7':
            return False
    return True


ans = 0
for i in range(1, n + 1):
    if check8(i) and check10(i):
        ans += 1

print(ans)
