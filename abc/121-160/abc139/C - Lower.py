n = int(input())
h = [int(x) for x in input().split()]

ans = 0
temp = 0

for i in range(1, n):
    if h[i - 1] >= h[i]:
        temp += 1
    else:
        temp = 0

    ans = max(ans, temp)

print(ans)
