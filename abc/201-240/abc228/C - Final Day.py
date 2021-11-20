import bisect

n, k = map(int, input().split())
p = [sum(map(int, input().split())) for _ in range(n)]
ppp = sorted(p)
for i in range(n):
    val = p[i] + 300
    idx = bisect.bisect_right(ppp, val)
    if n - idx < k:
        print('Yes')
    else:
        print('No')
