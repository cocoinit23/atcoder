import math

n = int(input())
r = sorted([int(input()) for _ in range(n)], reverse=True)

ans = 0
sign = True
for i in r:
    s = i * i * math.pi
    if sign:
        ans += s
    else:
        ans -= s

    sign = not sign

print(ans)
