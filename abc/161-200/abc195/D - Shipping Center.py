n, m, q = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]
wv = sorted(wv)
x = list(map(int, input().split()))
query = [list(map(int, input().split())) for _ in range(q)]

for l, r in query:
    temp = x.copy()
    temp[l - 1: r] = [0] * (r - l + 1)
    temp = sorted(temp)
    ans = 0
    used = [False] * n

    value = 0
    for i in temp:
        if i == 0:
            continue

        idx = -1
        val = 0
        weight = 1e7
        for j in range(n):
            w, v = wv[j]
            if w > i or used[j]:
                continue

            if v >= val:
                val = v
                idx = j

        if idx != -1:
            ans += val
            used[idx] = True

    print(ans)
