n, m = map(int, input().split())
a = []
for i in range(n):
    a += (list(map(int, input().split()))[1:])

ans = 0
for i in range(1, m + 1):
    if a.count(i) == n:
        ans += 1

print(ans)
