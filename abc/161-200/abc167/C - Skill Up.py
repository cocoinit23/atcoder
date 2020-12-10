import numpy as np

n, m, x = map(int, input().split())
ca = np.array([list(map(int, input().split())) for _ in range(n)])

pattern = []
for i in range(2 ** n):
    temp = [0] * n
    for j in range(n):
        if (i >> j) & 1:
            temp[j] = 1
    pattern.append(temp)

ans = 10 ** 10
for p in pattern:
    check = [0] * (m + 1)
    for i in range(n):
        if p[i] == 1:
            check += ca[i]
    flag = True
    for a in check[1:]:
        if a < x:
            flag = False
            break
    if flag:
        ans = min(ans, check[0])

print(ans) if ans != 10 ** 10 else print(-1)
