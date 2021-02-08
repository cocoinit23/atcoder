import bisect

n = int(input())
l = list(map(int, input().split()))
l.sort()

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        a = l[i]
        b = l[j]
        c = bisect.bisect_left(l, a + b) - 1
        ans += c - j
print(ans)
