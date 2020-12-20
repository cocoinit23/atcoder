n = int(input())
p = sorted([int(input()) for i in range(n)])

ans = p[-1] // 2 + sum(p[:-1])
print(ans)
