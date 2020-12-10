import math

n = int(input())
a = int(math.sqrt(n)) + 1

res = 10 ** 12

for i in range(1, a):
    if n % i == 0:
        b = n // i
        res = min(res, i + b - 2)

print(res)
