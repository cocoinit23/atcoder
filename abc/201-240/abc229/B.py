a, b = input().split()

keta = min(len(a), len(b))
a = a[::-1]
b = b[::-1]

ans = True
for i in range(keta):
    x = int(a[i])
    y = int(b[i])
    if x + y >= 10:
        ans = False
        break

print('Easy' if ans else 'Hard')
