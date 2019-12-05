from collections import Counter

kw = Counter()

n = int(input())

s = []
for _ in range(n):
    a = sorted(input())
    kw[''.join(a)] += 1

sum = 0
for _, val in kw.most_common():
    sum += val * (val - 1) // 2

print(sum)
