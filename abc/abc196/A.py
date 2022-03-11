a, b = map(int, input().split())
c, d = map(int, input().split())

x = max(a, b)
y = min(c, d)
ans = x - y
print(ans)
