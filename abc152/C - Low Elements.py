n = int(input())
p = [int(x) for x in input().split()]

ans = 1
base = p[0]

for i in range(1, n):
    if p[i] < base:
        ans += 1
        base = p[i]

print(ans)
