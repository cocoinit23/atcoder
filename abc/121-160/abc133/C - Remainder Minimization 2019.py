l, r = map(int, input().split())

if r - l >= 2019:
    print(0)
else:
    ans = 2018
    for i in range(l, r + 1):
        for j in range(l, r + 1):
            if i >= j:
                continue
            else:
                ans = min(ans, i * j % 2019)

    print(ans)
