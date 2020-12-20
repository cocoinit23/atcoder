import math
from scipy.spatial import distance

a, b, h, m = map(int, input().split())

jishin = math.radians(90 - (h + m / 60) * 30)
hunshin = math.radians(90 - m * 6)

x = (a * math.cos(jishin), a * math.sin(jishin))
y = (b * math.cos(hunshin), b * math.sin(hunshin))

ans = distance.euclidean(x, y)
print(ans)
