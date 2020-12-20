n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(1, n):
    candy = a[i - 1] + a[i]
    if candy > x:
        ans += candy - x
        a[i] = max(0, a[i] - candy + x)

print(ans)
