from collections import Counter

n = int(input())
a = list(map(int, input().split()))
prime = [1] * 1000010

for i in a:
    for j in range(i + i, 1000001, i):
        prime[j] = 0

c = Counter(a)
ans = 0
for i in a:
    if prime[i] and c[i] == 1:
        ans += 1
print(ans)
