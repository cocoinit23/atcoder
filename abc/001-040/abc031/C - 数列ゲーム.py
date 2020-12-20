n = int(input())
a = list(map(int, input().split()))

ans = -10 ** 10
for i in range(n):
    aoki = []
    for j in range(n):
        if i == j:
            continue

        l = min(i, j)
        r = max(i, j)
        t = a[l:r + 1]
        aoki.append(sum(t[1::2]))

    idx = aoki.index(max(aoki))
    l = min(i, idx)
    r = max(i, idx)
    t = a[l: r + 1]
    ans = max(ans, sum(t[0::2]))

print(ans)
