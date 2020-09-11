from collections import Counter

w = list(input())
c = Counter(w)
for v in c.values():
    if v % 2 != 0:
        print('No')
        exit()

print('Yes')
