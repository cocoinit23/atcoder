from collections import deque

n = int(input())
waza = [list(map(int, input().split())) for _ in range(n)]

learned = [False] * n

q = deque()
q.append(waza[-1])
ans = 0
while q:
    param = q.pop()
    t, k, a = param[0], param[1], param[2:]
    ans += t
    for i in a:
        if not learned[i - 1]:
            learned[i - 1] = True
            q.append(waza[i - 1])

print(ans)
