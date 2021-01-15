n = int(input())

l = 0
r = n + 1

while r - l > 1:
    mid = (l + r) // 2
    if mid * (mid + 1) // 2 <= n + 1:
        l = mid
    else:
        r = mid

ans = n - l + 1
print(ans)
