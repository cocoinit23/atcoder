"""
h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

ans = []
for i in range(w):
    temp = []
    for j in range(h):
        temp.append(a[j][i])
    ans.append(temp)

for i in ans:
    print(*i)
"""

import numpy as np

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
a = np.array(a)

ans = a.T
for i in ans:
    print(*i)
