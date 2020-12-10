n = int(input())
a = list(map(int, input().split()))
a = [a[i] - i - 1 for i in range(n)]

b = sorted(a)
if n % 2 != 0:
    b = b[n // 2]
else:
    b = (b[n // 2] + b[n // 2 - 1]) // 2

a = [abs(a[i] - b) for i in range(n)]
ans = sum(a)
print(ans)
