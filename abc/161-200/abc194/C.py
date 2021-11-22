n = int(input())
a = list(map(int, input().split()))

ans = (n - 1) * a[0] ** 2
cumsum = [0] * n
cumsum[0] = a[0]
for i in range(1, n):
    cumsum[i] = cumsum[i - 1] + a[i]
    ans += (n - 1) * a[i] ** 2

for i in range(n):
    ans -= 2 * a[i] * (cumsum[-1] - cumsum[i])

print(ans)
