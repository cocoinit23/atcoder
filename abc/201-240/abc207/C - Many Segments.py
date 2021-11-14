n = int(input())
tlr = [list(map(int, input().split())) for _ in range(n)]
tlr = sorted(tlr, key=lambda x: x[1])


def preprocess(x):
    t, l, r = x

    delta = 0.1
    if t == 1:
        pass
    elif t == 2:
        r -= delta
    elif t == 3:
        l += delta
    elif t == 4:
        l += delta
        r -= delta

    return l, r


ans = 0
for i in range(n):
    for j in range(i + 1, n):
        l1, r1 = preprocess(tlr[i])
        l2, r2 = preprocess(tlr[j])

        # if max(l1, l2) <= min(r1, r2):
        if not r1 < l2:
            ans += 1

print(ans)
