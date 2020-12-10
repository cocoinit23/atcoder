n, k = map(int, input().split())
h = [int(x) for x in input().split()]

if n <= k:
    print(0)
elif k != 0:
    h.sort()
    ans = sum(h[:-k])
    print(ans)
else:
    print(sum(h))
