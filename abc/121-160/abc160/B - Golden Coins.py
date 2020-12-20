x = int(input())

a = x // 500
x %= 500

b = x // 5

ans = a * 1000 + b * 5
print(ans)
