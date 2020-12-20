from collections import Counter

n = int(input())
a = list(map(int, input().split()))

c = Counter(a).most_common()
edge = sorted([key, val] for key, val in c if val >= 2)

if len(edge) < 2:
    ans = 0
elif edge[-1][1] >= 4:
    ans = edge[-1][0] ** 2
else:
    ans = edge[-1][0] * edge[-2][0]

print(ans)
