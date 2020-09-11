n = int(input())
a = [x for x in map(int, input().split())]
b = [x for x in map(int, input().split())]

ans = 0

for i in range(n):
    if a[i] <= b[i]:
        ans += a[i]
        b[i] -= a[i]
        a[i] = 0
        if b[i] == 0:
            continue
        else:
            if a[i + 1] <= b[i]:
                ans += a[i + 1]
                a[i + 1] = 0
                b[i] = 0
            else:
                ans += b[i]
                a[i + 1] -= b[i]
                b[i] = 0

    else:
        ans += b[i]
        a[i] -= b[i]

print(ans)
