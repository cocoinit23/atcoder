import heapq

h, w, t = map(int, input().split())
s = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == 'S':
            sy, sx = i, j
        if s[i][j] == 'G':
            gy, gx = i, j


def dijkstra(x):
    cost = [[1e20] * w for _ in range(h)]
    cost[sy][sx] = 0
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    q = []
    heapq.heapify(q)
    heapq.heappush(q, [sy, sx])
    while q:
        cy, cx = heapq.heappop(q)
        for i, j in move:
            ny = cy + i
            nx = cx + j
            if 0 <= nx < w and 0 <= ny < h:
                if s[ny][nx] == '#':
                    if cost[ny][nx] > cost[cy][cx] + x:
                        cost[ny][nx] = cost[cy][cx] + x
                        heapq.heappush(q, [ny, nx])
                else:
                    if cost[ny][nx] > cost[cy][cx] + 1:
                        cost[ny][nx] = cost[cy][cx] + 1
                        heapq.heappush(q, [ny, nx])

    return cost[gy][gx] <= t


l = 0
r = t
while r - l > 1:
    mid = (l + r) // 2
    if dijkstra(mid):
        l = mid
    else:
        r = mid

print(l)
