from decimal import Decimal

a, b = input().split()
a = Decimal(a)
b = Decimal(b)

ans = (a * b) // 1
print(ans)
