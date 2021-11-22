n, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x: x[0])

ans = 0
prev = 0

for a, b in ab:
    diff = a - prev

    if k - diff < 0:
        break

    if a == prev:
        k += b
        continue

    k -= diff
    ans += diff
    k += b
    prev = a

ans += k
print(ans)
