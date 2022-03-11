def inv(x):
    return 1 / x


n = int(input())
a = [int(x) for x in input().split()]

sum = 0
for i in range(n):
    sum += inv(a[i])

print(inv(sum))
