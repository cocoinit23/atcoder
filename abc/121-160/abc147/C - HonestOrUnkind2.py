n = int(input())

a = []
xy = []

for i in range(n):
    a.append(int(input()))
    temp = []
    for j in range(a[i]):
        temp.append(list(map(int, input().split())))
    xy.append(temp)

ans = 0

for i in range(2 ** n):
    memo = [1] * n
    for j in range(n):
        if (i >> j) & 1:
            memo[n - j - 1] = 0

    for p in range(n):
        flag = True
        for q in range(a[p]):
            x = xy[p][q][0] - 1
            y = xy[p][q][1]
            if memo[p] == 1 and memo[x] != y:
                flag = False
                break
        if not flag:
            break

    if flag:
        ans = max(ans, memo.count(1))

print(ans)
