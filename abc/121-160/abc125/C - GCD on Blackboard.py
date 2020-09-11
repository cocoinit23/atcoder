from fractions import gcd

n = int(input())
a = [int(x) for x in input().split()]

left = [0] * (n + 1)
right = [0] * (n + 1)

for i in range(n):
    left[i + 1] = gcd(left[i], a[i])

for i in reversed(range(n)):
    right[i] = gcd(right[i + 1], a[i])

ans = 0
for i in range(n):
    ans = max(ans, gcd(left[i], right[i + 1]))

print(ans)
