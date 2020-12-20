from collections import Counter

n = int(input())
a = list(map(int, input().split()))

x = []
for i in a:
    x.append(i)
    x.append(i + 1)
    x.append(i - 1)

ans = max(Counter(x).values())
print(ans)
