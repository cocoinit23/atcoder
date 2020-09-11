from collections import Counter

n = int(input())
a = list(map(int, input().split()))

if len(a) == len(set(a)):
    for i in range(n):
        print(0)
else:
    kw = Counter(a)
    ans = sum([x * (x - 1) // 2 for x in kw.values()])

    for i in range(n):
        print(ans - kw[a[i]] + 1)
