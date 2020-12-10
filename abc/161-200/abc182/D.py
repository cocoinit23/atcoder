import numpy as np

n = int(input())
a = list(map(int, input().split()))

totalMove = 0
maxMove = 0
now = 0
ans = 0

for i in a:
    totalMove += i
    maxMove = max(maxMove, totalMove)
    ans = max(ans, now + maxMove)
    now += totalMove

print(ans)
