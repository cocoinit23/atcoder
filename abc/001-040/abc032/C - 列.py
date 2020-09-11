n, k = map(int, input().split())
s = [int(input()) for _ in range(n)]

ans = 0
r = 0
val = 1
for l in range(n):
    if s[l] == 0:
        ans = n
        break

    while r < n and val * s[r] <= k:
        val *= s[r]
        r += 1
    ans = max(ans, r - l)

    if l == r:
        r += 1
    else:
        val /= s[l]

print(ans)
