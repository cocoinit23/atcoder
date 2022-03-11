sx, sy, gx, gy = map(int, input().split())

grad = (sy + gy) / (gx - sx)
ans = sy / grad + sx
print(ans)
