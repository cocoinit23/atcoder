from collections import Counter
from itertools import permutations

s = list(input())
s = Counter(s)

num = []
for key, val in s.most_common():
    for i in range(min(3, val)):
        num.append(int(key))

ans = False
for l in permutations(num, min(3, len(num))):
    keta = 1
    temp = 0
    for i in l:
        temp += keta * i
        keta *= 10
    if temp % 8 == 0:
        ans = True
        break

print('Yes') if ans else print('No')
