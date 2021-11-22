import math

n = int(input())

ans = set()
for a in range(2, 10 ** 5 + 1):
    limit = int(math.log(10 ** 10, a))
    for b in range(2, limit + 1):
        if 1 <= a ** b <= n:
            ans.add(a ** b)

ans = n - len(ans)
print(ans)
