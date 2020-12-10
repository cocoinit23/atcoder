from collections import deque


def bfs(maze, x, y):
    m = [1, 0, -1, 0]
    n = [0, 1, 0, -1]
    queue = deque([[x, y]])
    dist = [[-1] * (w + 2) for _ in range(h + 2)]
    dist[x][y] = 0

    while queue:
        sx, sy = queue.popleft()

        for dx, dy in zip(m, n):
            nx = sx + dx
            ny = sy + dy
            if maze[nx][ny] != '#' and dist[nx][ny] == -1:
                queue.append([nx, ny])
                dist[nx][ny] = dist[sx][sy] + 1

    return max(max(x) for x in dist)


h, w = map(int, input().split())

maze = [['#'] * (w + 2)]
for i in range(h):
    maze.append(['#'] + list(map(str, input())) + ['#'])

maze.append(['#'] * (w + 2))

ans = 0
for sy in range(1, w + 1):
    for sx in range(1, h + 1):
        if maze[sx][sy] != '#':
            ans = max(ans, bfs(maze, sx, sy))

print(ans)
