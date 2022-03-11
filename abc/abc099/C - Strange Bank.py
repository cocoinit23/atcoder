n = int(input())
num = [1]

x = 6
while x < 100000:
    num.append(x)
    x *= 6

x = 9
while x < 100000:
    num.append(x)
    x *= 9

dp = [n] * 1100000
dp[0] = 0

for i in range(n):
    for j in num:
        dp[i + j] = min(dp[i + j], dp[i] + 1)

print(dp[n])
