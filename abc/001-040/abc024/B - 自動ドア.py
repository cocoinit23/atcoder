n, t = map(int, input().split())
a = [int(input()) for _ in range(n)]

ans = 0
for i in range(1, n):
    diff = a[i] - a[i - 1]
    if diff >= t:
        ans += t
    else:
        ans += diff

print(ans + t)
