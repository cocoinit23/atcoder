from collections import deque

n, m = map(int, input().split())

if m == 0:
    ans = n
else:
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    ans = 0
    for start in range(1, n + 1):
        canVisit = [False] * (n + 1)
        q = deque()
        q.append(start)
        while q:
            cur = q.pop()
            if not canVisit[cur]:
                canVisit[cur] = True
                for i in graph[cur]:
                    q.append(i)

        ans += sum(canVisit)

print(ans)
