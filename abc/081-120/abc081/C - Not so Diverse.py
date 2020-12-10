from collections import Counter

n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
if k < len(Counter(a).keys()):
    kv = Counter(a).most_common()
    for i in range(1, len(Counter(a).keys()) - k + 1):
        ans += kv[-i][1]

print(ans)
