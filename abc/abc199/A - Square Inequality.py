a, b, c = map(int, input().split())
ans = a ** 2 + b ** 2 < c ** 2
print("Yes" if ans else "No")
