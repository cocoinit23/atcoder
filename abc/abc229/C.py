n, w = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

ab.sort(reverse=True)

ans = 0
for a, b in ab:
    if w >= b:
        w -= b
        ans += a * b
    else:
        ans += a * w
        break

print(ans)
