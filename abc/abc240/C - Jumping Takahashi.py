n, x = map(int, input().split())

dp = 1
for i in range(n):
    a, b = map(int, input().split())
    a = dp << a
    b = dp << b
    dp = a | b

ans = (dp >> x) & 1
print('Yes' if ans else 'No')

"""
n, x = map(int, input().split())

dp = [[False] * (x + 1) for _ in range(n + 1)]
dp[0][0] = True

for i in range(n):
    a, b = map(int, input().split())
    for j in range(x + 1):
        if dp[i][j]:
            if j + a <= x:
                dp[i + 1][j + a] = True
            if j + b <= x:
                dp[i + 1][j + b] = True
ans = dp[n][x]
print('Yes' if ans else 'No')
"""

"""
n, x = map(int, input().split())

pos = [0]
for _ in range(n):
    a, b = map(int, input().split())
    temp = []
    for i in pos:
        if i + a <= x:
            temp.append(i + a)
        if i + b <= x:
            temp.append(i + b)

    pos = list(set(temp))
    if not pos:
        break

print('Yes' if x in pos else 'No')
"""
