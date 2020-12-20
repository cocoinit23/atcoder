n, h = map(int, input().split())
a, b, c, d, e = map(int, input().split())

ans = 1e20
for i in range(n + 1):
    j = n - i
    hangry = h + i * b

    if hangry > j * e:
        k = 0
    else:
        val = (n * e - h - i * (b + e)) // (d + e) + 1
        k = max(0, val)

    cost = a * i + c * k
    ans = min(ans, cost)

print(ans)
