n = int(input())
p = [0] + list(map(int, input().split()))

ans = 0
for i in range(1, n + 1):
    if i < n and i == p[i]:
        p[i], p[i + 1] = p[i + 1], p[i]
        ans += 1
    elif i == n and i == p[i]:
        ans += 1

print(ans)
