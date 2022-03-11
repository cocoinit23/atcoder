from scipy.spatial import distance
import math

r, x, y = map(int, input().split())

n = distance.euclidean((0, 0), (x, y))
if n == r:
    ans = 1
elif n < r:
    ans = 2
else:
    ans = math.ceil(n / r)

print(ans)
