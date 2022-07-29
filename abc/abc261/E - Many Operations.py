n, c = map(int, input().split())
x = c

zero = 0
one = ~0

for i in range(n):
    t, a = map(int, input().split())

    if t == 1:
        zero &= a
        one &= a
    elif t == 2:
        zero |= a
        one |= a
    else:
        zero ^= a
        one ^= a

    x = (one & x) | (zero & ~x)

    print(x)
