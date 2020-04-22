from collections import deque

n, x, y = map(int, input().split())

inf = 100100100
x -= 1
y -= 1

ans = [0] * n

for i in range(n):
    dist = [inf] * n
    queue = deque()
    queue.append(i)
    dist[i] = 0
    while queue:
        current = queue.popleft()
        d = dist[current]

        if current - 1 >= 0 and dist[current - 1] == inf:
            queue.append(current - 1)
            dist[current - 1] = d + 1
        if current + 1 < n and dist[current + 1] == inf:
            queue.append(current + 1)
            dist[current + 1] = d + 1
        if current == x and dist[y] == inf:
            queue.append(y)
            dist[y] = d + 1
        if current == y and dist[x] == inf:
            queue.append(x)
            dist[x] = d + 1

    for j in range(n):
        ans[dist[j]] += 1

for k in range(1, n):
    print(ans[k] // 2)
