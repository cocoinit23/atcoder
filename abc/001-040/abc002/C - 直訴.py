xa, ya, xb, yb, xc, yc = map(int, input().split())

s = abs(xa * yb + xb * yc + xc * ya - ya * xb - yb * xc - yc * xa) / 2
print(s)
