n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)

cumsum = [0] * n
cumsum[0] = a[0]
for i in range(1, n):
    cumsum[i] = cumsum[i - 1] + a[i]

ans = 0
for i in range(n - 1):
    ans += a[i] * (n - 1 - i)
    ans -= cumsum[-1] - cumsum[i]

print(ans)
