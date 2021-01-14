n, c = map(int, input().split())

event = []
for _ in range(n):
    a, b, q = map(int, input().split())
    event.append([a - 1, q])
    event.append([b, -q])

event.sort()

ans = 0
fee = 0
time = 0

for x, y in event:
    if x != time:
        ans += min(c, fee) * (x - time)
        time = x
    fee += y

print(ans)
