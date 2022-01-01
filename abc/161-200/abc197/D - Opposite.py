import numpy as np

n = int(input())
x0, y0 = map(int, input().split())
xn2, yn2 = map(int, input().split())

xo = (x0 + xn2) / 2
yo = (y0 + yn2) / 2

x0 -= xo
y0 -= yo

angle = 360 / n
radian = np.deg2rad(angle)
cos = np.cos(radian)
sin = np.sin(radian)

x = x0 * cos - y0 * sin
y = x0 * sin + y0 * cos

x += xo
y += yo

print(x, y)
