from collections import deque

r, c = map(int, input().split())
sy, sx = map(lambda x: int(x) - 1, input().split())
gy, gx = map(lambda x: int(x) - 1, input().split())
maze = [list(input()) for _ in range(r)]

dist = [[1e9] * c for _ in range(r)]
dist[sy][sx] = 0

move = [[0, 1], [1, 0], [-1, 0], [0, -1]]
q = deque()
q.append([sx, sy])
while q:
    cx, cy = q.popleft()
    d = dist[cy][cx]
    for i, j in move:
        nx = cx + i
        ny = cy + j
        if [nx, ny] == [gx, gy]:
            print(d + 1)
            exit()
        if maze[ny][nx] == '.' and dist[ny][nx] > d + 1:
            q.append([nx, ny])
            dist[ny][nx] = d + 1
