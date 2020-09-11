n = int(input())
h = [int(x) for x in input().split()]

ans = 1
high = h[0]
for i in range(1, n):
    if h[i] >= high:
        ans += 1
        high = h[i]

print(ans)
