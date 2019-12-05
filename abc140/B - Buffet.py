n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

res = 0

for i in range(n):
    x = a[i] - 1
    res += b[x]

    if i < n - 1 and a[i] + 1 == a[i + 1]:
        res += c[x]

print(res)
