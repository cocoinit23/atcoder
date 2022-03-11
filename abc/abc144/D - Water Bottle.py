import math

a, b, x = map(int, input().split())
x /= a

if x > a * b / 2:
    tan = 2 * (a * b - x) / a ** 2
else:
    tan = b ** 2 / 2 / x

ans = math.degrees(math.atan(tan))
print(ans)
