n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

for i in range(n - m + 1):
    for j in range(n - m + 1):
        check = [a[i + k][j:j + m] for k in range(m)]

        flag = True
        for x in range(m):
            if check[x] != b[x]:
                flag = False
                break

        if flag:
            print('Yes')
            exit()

print('No')
