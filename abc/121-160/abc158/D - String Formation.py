from collections import deque

s = deque(input())
q = int(input())
query = [input().split() for _ in range(q)]

reverse = False

for i in range(q):
    now = query[i]
    if now == ['1']:
        reverse = not reverse
    else:
        f = now[1]
        c = now[2]
        if f == '1':
            s.append(c) if reverse else s.appendleft(c)
        else:
            s.appendleft(c) if reverse else s.append(c)

if reverse:
    s.reverse()

print(''.join(s))
