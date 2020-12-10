n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    x = a[i]
    while x % 2 == 0:
        x //= 2
    a[i] = x

ans = len(set(a))
print(ans)
