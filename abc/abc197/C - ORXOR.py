n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(a[0])
    exit()

if n == 2:
    ans = a[0] ^ a[1]
    print(ans)
    exit()

ans = 1e9
for i in range(1, 2 ** (n - 1) - 1):
    pattern = [0] * (n - 1)
    for j in range(n - 1):
        if i >> j & 1:
            pattern[j] = 1

    orval = a[0]
    xorval = 0
    for j in range(n - 1):
        if pattern[j] == 0:
            orval |= a[j + 1]
        else:
            xorval ^= orval
            orval = a[j + 1]

        if j == n - 2:
            orval |= a[j + 1]
            xorval ^= orval

    ans = min(ans, xorval)

print(ans)
