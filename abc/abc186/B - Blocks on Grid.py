h, w = map(int, input().split())
a = []
for _ in range(h):
    a += list(map(int, input().split()))

low = min(a)

ans = sum([i - low for i in a])
print(ans)
