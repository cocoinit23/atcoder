n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i, n):
        ans = max(ans, abs(a[i] - a[j]))

print(ans)
