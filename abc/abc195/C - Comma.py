n = int(input())
ans = 0

val = 1000
while val <= n:
    if n >= val:
        ans += n - val + 1
        val *= 1000

print(ans)
