from collections import deque

k = int(input())
limit = 10

start = [i for i in range(1, 10)]
q = deque(start)
ans = []

while q:
    cur = q.popleft()
    if len(str(cur)) > 11:
        continue
    ans.append(cur)
    r = str(cur)[-1]
    if r == '0':
        add = ['0', '1']
    elif r == '9':
        add = ['8', '9']
    else:
        add = [str(int(r) - 1), str(int(r)), str(int(r) + 1)]

    for i in add:
        q.append(int(str(cur) + i))

ans = sorted(ans)
print(ans[k - 1])
