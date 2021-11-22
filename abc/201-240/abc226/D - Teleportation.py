import math

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

magic = []

for i in range(n):
    for j in range(n):
        if i == j:
            continue

        x1, y1 = xy[i]
        x2, y2 = xy[j]

        dist_x = x1 - x2
        dist_y = y1 - y2
        gcd = math.gcd(dist_x, dist_y)
        dist_x /= gcd
        dist_y /= gcd

        magic.append((dist_x, dist_y))
        magic.append((-dist_x, -dist_y))

magic = set(magic)
ans = len(magic)
print(ans)
