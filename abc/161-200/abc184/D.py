import numpy as np

a, b, c = map(int, input().split())

ans = 0
dp = np.zeros((110, 110, 110))

for i in range(c, 101):
    for j in range(b, 101):
        for k in range(a, 101):
            p = dp[i][j][k]
            print(i,j,k,p)
            denominator = i + j + k
            if a != 0:
                dp[i + 1][j][k] = p + i / denominator
            if b != 0:
                dp[i][j + 1][k] = p + j / denominator
            if c != 0:
                dp[i][j][k + 1] = p + k / denominator

ans = dp[100, 100, 100]
print(ans)
