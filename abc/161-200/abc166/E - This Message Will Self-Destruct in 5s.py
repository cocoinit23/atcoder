from collections import Counter

n = int(input())
a = list(map(int, input().split()))

x = [0] * n
y = [0] * n
for i in range(n):
    x[i] = i + a[i]
    y[i] = i - a[i]

cx = Counter(x)
cy = Counter(y)

ans = 0
for i in cx.keys():
    ans += cx[i] * cy[i]

print(ans)

print(cx)
print(cy)
