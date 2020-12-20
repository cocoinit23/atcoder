n, k = map(int, input().split())
a = list(map(int, input().split()))

cumsum = [0] * (n + 1)
for i in range(n):
    cumsum[i + 1] = cumsum[i] + a[i]

ans = 0
for i in range(k, n + 1):
    ans += cumsum[i] - cumsum[i - k]

print(ans)
