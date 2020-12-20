from collections import deque

h, w = map(int, input().split())
ch, cw = map(lambda x: int(x) - 1, input().split())
dh, dw = map(lambda x: int(x) - 1, input().split())
maze = [list(input()) for _ in range(h)]

inf = 10 ** 10
cost = [[inf] * w for _ in range(h)]

walk = [[0, 1], [0, -1], [1, 0], [-1, 0]]
warp = [[i, j] for i in range(-2, 3) for j in range(-2, 3) if [i, j] not in [[0, 0]] + walk]

q = deque()
cost[ch][cw] = 0
q.append([ch, cw, 0])

while q:
    x, y, c = q.popleft()
    for dx, dy in walk:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] == '.' and cost[nx][ny] > c:
            cost[nx][ny] = c
            q.appendleft([nx, ny, c])

    for dx, dy in warp:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] == '.' and cost[nx][ny] > c + 1:
            cost[nx][ny] = c + 1
            q.append([nx, ny, c + 1])

ans = cost[dh][dw] if cost[dh][dw] != inf else -1
print(ans)
