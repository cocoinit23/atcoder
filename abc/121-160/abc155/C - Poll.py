from collections import Counter

n = int(input())

kw = Counter()
for i in range(n):
    s = input()
    kw[s] += 1

v = max(kw.values())
ans = []

for key, value in kw.most_common():
    if value == v:
        ans.append(key)

for s in sorted(ans):
    print(s)
