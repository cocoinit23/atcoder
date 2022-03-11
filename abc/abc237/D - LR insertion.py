"""
from collections import deque

n = int(input())
s = input()

ans = deque([n])

for i in range(n - 1, -1, -1):
    if s[i] == 'R':
        ans.appendleft(i)
    else:
        ans.append(i)

print(*ans)
"""

n = int(input())
s = input()
l = []
r = []

for i, c in enumerate(s):
    if c == 'L':
        r.append(i)
    else:
        l.append(i)

ans = l + [n] + r[::-1]
print(*ans)
