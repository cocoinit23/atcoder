import math
import itertools

n = int(input())

xy = []
for i in range(n):
    x, y = map(float, input().split())
    xy.append([x, y])

l = list(itertools.permutations(xy, 2))

res = 0
for i in range(len(l)):
    x1, x2 = l[i][0][0], l[i][1][0]
    y1, y2 = l[i][0][1], l[i][1][1]

    res += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

print(res / n)
