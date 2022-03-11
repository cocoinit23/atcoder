from collections import Counter

r, c, k = map(int, input().split())
n = int(input())

coord = []
candies_r = [0] * r
candies_c = [0] * c

for _ in range(n):
    r, c = map(lambda x: int(x) - 1, input().split())
    coord.append([r, c])
    candies_r[r] += 1
    candies_c[c] += 1

ans = 0
nr = Counter(candies_r)
nc = Counter(candies_c)
for i in range(k + 1):
    ans += nr[i] * nc[k - i]

for x, y in coord:
    temp = candies_r[x] + candies_c[y]
    if temp == k:
        ans -= 1
    elif temp == k + 1:
        ans += 1

print(ans)
