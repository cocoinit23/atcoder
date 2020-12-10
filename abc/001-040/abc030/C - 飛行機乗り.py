import bisect

n, m = map(int, input().split())
x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
now = 0

while True:
    id = bisect.bisect_left(a, now)
    if id >= n:
        break
    now = a[id] + x

    id = bisect.bisect_left(b, now)
    if id >= m:
        break
    now = b[id] + y
    ans += 1

print(ans)
