from collections import Counter

s = [i for i in input()]
t = [i for i in input()]

ss = Counter(s)
tt = Counter(t)

if sorted(ss.values()) == sorted(tt.values()):
    print('Yes')
else:
    print('No')
