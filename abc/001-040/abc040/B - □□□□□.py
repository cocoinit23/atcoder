n = int(input())

ans = 10 ** 10
limit = int(n ** 0.5)

for i in range(1, n + 1):
    for j in range(1, n // i + 1):
        if 0 < i * j <= n:
            rest = n - i * j
            ans = min(ans, abs(i - j) + rest)

print(ans)
