n = int(input())

if n == 0:
    print(0)
else:
    s = ''

    while n != 0:
        s = str(abs(n % -2)) + s
        if n % -2 != 0:
            n //= -2
            n += 1
        else:
            n //= -2

    print(s)
