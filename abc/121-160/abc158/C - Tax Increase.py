import math

a, b = map(int, input().split())
limit = int(100 / 0.08) + 1
ans = limit

for i in range(1, limit):
    x = math.floor(i * 0.08)
    y = math.floor(i * 0.1)
    if x == a and y == b:
        ans = min(ans, i)

print(ans) if not ans == limit else print(-1)
