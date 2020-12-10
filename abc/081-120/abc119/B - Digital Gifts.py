n = int(input())

jpy = 0
btc = 0
for i in range(n):
    x, u = input().split()
    if u == 'JPY':
        jpy += float(x)
    else:
        btc += float(x)

ans = jpy + 380000 * btc
print(ans)
