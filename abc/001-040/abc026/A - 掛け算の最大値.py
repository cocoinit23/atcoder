a = int(input())

ans = 0
for i in range(a + 1):
    for j in range(a + 1 - i):
        ans = max(ans, i * j)

print(ans)
