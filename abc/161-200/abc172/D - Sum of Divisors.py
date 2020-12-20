n = int(input())

ans = 0
for i in range(1, n + 1):
    limit = n // i
    ans += (limit * (limit + 1) // 2) * i

print(ans)
