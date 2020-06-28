from collections import Counter

n = int(input())
a = list(map(int, input().split()))
q = int(input())
bc = [list(map(int, input().split())) for _ in range(q)]

x = Counter(a)
ans = sum(a)
for b, c in bc:
    ans += (c - b) * x[b]
    print(ans)
    x[c] += x[b]
    x[b] = 0
