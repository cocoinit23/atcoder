n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

ans = 1e9
for i in range(n):
    for j in range(n):
        a = ab[i][0]
        b = ab[j][1]
        if i == j:
            ans = min(ans, a + b)
        else:
            ans = min(ans, max(a, b))
print(ans)
