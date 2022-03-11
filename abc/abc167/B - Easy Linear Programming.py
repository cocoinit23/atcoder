a, b, c, k = map(int, input().split())

ans = 0
if k < a:
    ans += k
else:
    ans += a
    k -= a
    if k >= b:
        k -= b
        if k > c:
            ans -= c
        else:
            ans -= k

print(ans)
