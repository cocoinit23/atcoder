n = int(input())
a = list(map(int, input().split()))

ans = 0
for l in range(n):
    x = a[l]
    for r in range(l, n):
        x = min(x, a[r])
        ans = max(ans, (r - l + 1) * x)
print(ans)
# O(N^2) -> Python3 TLE
# pypy3 OK