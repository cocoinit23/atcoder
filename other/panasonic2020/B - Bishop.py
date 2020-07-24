import math

h, w = map(int, input().split())

if h == 1 or w == 1:
    ans = 1
elif (h * w) % 2 == 0:
    ans = (h * w) // 2
else:
    ans = (h // 2) * w + math.ceil(w / 2)

print(ans)
