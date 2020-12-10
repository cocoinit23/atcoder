n, k = map(int, input().split())
a = list(map(int, input().split()))

visited = [0] * (n + 1)
now = 1
check = 2 * n
loop_start = 1
while check > 0:
    if visited[now - 1] == 1:
        loop_start = now
        break
    else:
        visited[now - 1] += 1
        now = a[now - 1]
        check -= 1

visited = [0] * (n + 1)
now = loop_start
check = n
loop = 0
while check > 0:
    if visited[now - 1] == 1:
        break
    else:
        visited[now - 1] += 1
        now = a[now - 1]
        check -= 1
        loop += 1

now = 1
while k > 0:
    if now == loop_start:
        k %= loop
        if k == 0:
            break
    now = a[now - 1]
    k -= 1

print(now)
