n = int(input())
a = list(map(int, input().split()))

ans = 1
gcd_like = 0
for i in range(2, max(a) + 1):
    cnt = 0
    for j in range(n):
        if a[j] % i == 0:
            cnt += 1
    if cnt >= gcd_like:
        gcd_like = cnt
        ans = i

print(ans)
