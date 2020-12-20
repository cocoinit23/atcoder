n, m = map(int, input().split())

if 2 * n <= m <= 4 * n:
    for x in range(n + 1):
        y = m % 2
        z = n - y - x
        if 2 * x + 3 * y + 4 * z == m:
            print(x, y, z)
            exit()

    print(-1, -1, -1)
else:
    print(-1, -1, -1)
