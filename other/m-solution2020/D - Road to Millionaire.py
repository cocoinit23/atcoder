n = int(input())
a = [0] + list(map(int, input().split()))

dp = [0] * (n + 10)
dp[1] = 1000
for i in range(2, n + 1):
    dp[i] = dp[i - 1]
    for j in range(1, i):
        x = dp[j] // a[j]
        y = dp[j] + (a[i] - a[j]) * x
        dp[i] = max(dp[i], y)

ans = dp[n]
print(ans)

'''
n = int(input())
a = list(map(int, input().split()))

ans = 1000
for i in range(n - 1):
    x = a[i]
    y = a[i + 1]
    if x < y:
        k = ans // x
        ans %= x
        ans += k * y

print(ans)
'''
