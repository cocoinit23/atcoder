n, k = map(int, input().split())
p = [None] + list(map(int, input().split()))
c = [None] + list(map(int, input().split()))

ans = []
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    move = k
    point = 0
    loop = 0
    loop_point = 0
    now = i
    visited[i] = True

    while move > 0:
        move -= 1
        now = p[now]
        point += c[now]
        loop += 1
        loop_point += c[now]
        ans.append(point)
        if visited[now]:
            point += loop_point * (move // loop)
            ans.append(point)
            move %= loop
            visited = [False] * (n + 1)
            loop_point = 0
            break
        else:
            visited[now] = True

print(max(ans))
