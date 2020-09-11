n = int(input())
csf = [list(map(int, input().split())) for _ in range(n - 1)]

for i in range(n):
    t = 0
    for j in range(i, n - 1):
        c, s, f = csf[j]
        if t < s:
            t = s
        elif t % f == 0:
            pass
        else:
            t += f - t % f

        t += c

    print(t)
