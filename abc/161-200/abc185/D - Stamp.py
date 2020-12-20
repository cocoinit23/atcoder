import math

n, m = map(int, input().split())
a = list(map(int, input().split()))

if m == 0:
    print(1)
    exit()

if 1 not in a:
    a.append(0)
if n not in a:
    a.append(n + 1)

a.sort()

diff = [0] * (len(a) - 1)
for i in range((len(a) - 1)):
    diff[i] = a[i + 1] - a[i] - 1

k = set(diff)
if k == {0}:
    print(0)
    exit()

if 0 in k:
    k.remove(0)
if len(k) == 0:
    print(0)
    exit()

k = min(k)

ans = sum([math.ceil(i / k) for i in diff])
print(ans)
