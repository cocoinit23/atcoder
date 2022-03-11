a, b = map(int, input().split())
a, b = max(a, b), min(a, b)

coin = 0
coin += a
a -= 1

if a >= b:
    coin += a
else:
    coin += b

print(coin)
