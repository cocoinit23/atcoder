a, b, k, l = map(int, input().split())

ans = 0
if b / l < a:
    ans += b * (k // l)
    k -= l * (k // l)
    if k * a < b:
        ans += a * k
    else:
        ans += b
else:
    ans = k * a
print(ans)
