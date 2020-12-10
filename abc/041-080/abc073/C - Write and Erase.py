from collections import Counter

n = int(input())
a = [int(input()) for _ in range(n)]

c = Counter(a)

ans = 0
for key, value in c.most_common():
    if value % 2 != 0:
        ans += 1

print(ans)
