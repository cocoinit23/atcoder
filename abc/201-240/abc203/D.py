import numpy as np

n, k = map(int, input().split())
# a = np.array([list(map(int, input().split())) for _ in range(n)])
target = (k ** 2) // 2 + 1

a = np.random.randint(0, 1e9, (n, n))
print(a)

ans = []
for i in range(n - k + 1):
    for j in range(n - k + 1):
        pond = a[i:i + k, j:j + k]
        h = np.sort(pond.ravel())[-target]
        ans.append(h)

print(min(ans))
