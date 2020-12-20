n = int(input())
a = list(map(int, input().split()))

ans = 0
h = a[0]
for i in a[1:]:
    if i <= h:
        ans += h - i
    else:
        h = i

print(ans)