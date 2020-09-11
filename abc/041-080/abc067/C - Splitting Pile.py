n = int(input())
a = list(map(int, input().split()))

cumsum = [0] * (n + 1)
for i in range(n):
    cumsum[i + 1] = cumsum[i] + a[i]

ans = 10 ** 10
for i in range(1, n):
    x = cumsum[i]
    y = cumsum[n] - x
    ans = min(ans, abs(x - y))

print(ans)
