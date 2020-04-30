s = input()
n = len(s)
mod = 2019

total = [0] * (n + 1)
cnt = [0] * mod

for i in range(1, n + 1):
    now = int(s[n - i:])
    now %= mod
    cnt[now] += 1

print(total)
print(cnt)

from collections import Counter

print(Counter(cnt))
