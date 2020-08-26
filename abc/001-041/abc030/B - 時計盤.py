n, m = map(int, input().split())

if n >= 12:
    n -= 12

jishin = n * 30 + m * 0.5
hunshin = m * 6

ans = abs(jishin - hunshin)
ans = min(ans, abs(360 - ans))
print(ans)
