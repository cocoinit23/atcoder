n, m = map(int, input().split())
l = 1
r = n
for i in range(m):
    a, b = map(int, input().split())
    l = max(l, a)
    r = min(r, b)

if l <= r:
    print(r - l + 1)
else:
    print(0)
