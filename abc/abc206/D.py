import numpy as np

n = int(input())
a = np.array(list(map(int, input().split())))

if n == 1:
    ans = 0
else:
    if n % 2 == 0:
        left = a[:n // 2]
        right = a[n // 2:][::-1]
    else:
        left = a[:n // 2 + 1]
        right = a[n // 2:][::-1]

    ans = left != right
    ans = ans.sum() - 1

print(ans)
