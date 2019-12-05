x = int(input())

dp = [0] * 100001

dp[100] = dp[101] = dp[102] = dp[103] = dp[104] = dp[105] = 1

for i in range(106, 100001):
    if dp[i - 100] == 1 or dp[i - 101] == 1 or dp[i - 102] == 1 or dp[i - 103] == 1 or dp[i - 104] == 1 or dp[
        i - 105] == 1:
        dp[i] = 1

print(dp[x])
