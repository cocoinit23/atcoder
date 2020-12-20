n = int(input())

ans = 0
for i in range(int(n ** 0.5) + 1):
    if i ** 2 <= n:
        ans = max(ans, i ** 2)

print(ans)
