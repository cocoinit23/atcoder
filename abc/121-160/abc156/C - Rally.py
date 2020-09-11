import numpy as np

n = int(input())
x = np.array([int(x) for x in input().split()])

ans = 10 ** 10
for i in range(1, 101):
    temp = x - i
    ans = min(ans, sum([j ** 2 for j in temp]))

print(ans)
