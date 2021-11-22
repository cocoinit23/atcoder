from collections import Counter

n = int(input())
a = list(map(int, input().split()))

c = Counter(a)

ans = n * (n - 1) // 2
for k, v in c.most_common():
    ans -= v * (v - 1) // 2
print(ans)
