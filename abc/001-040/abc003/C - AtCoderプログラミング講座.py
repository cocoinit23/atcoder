n, k = map(int, input().split())
r = list(map(int, input().split()))

ans = 0
for i in sorted(r)[-k:]:
    ans = (ans + i) / 2

print(ans)
