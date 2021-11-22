n, m = map(int, input().split())

b = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m - 1):
        if (b[i][j + 1] - 1) % 7 - (b[i][j] - 1) % 7 != 1:
            print('No')
            exit()

for i in range(n - 1):
    for j in range(m):
        if b[i + 1][j] - b[i][j] != 7:
            print('No')
            exit()

    if b[i + 1][0] - b[i][-1] != 7 - m + 1:
        print('No')
        exit()

print('Yes')
