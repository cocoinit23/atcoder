n = int(input())
buka = [[] for _ in range(n + 1)]

for i in range(2, n + 1):
    b = int(input())
    buka[b].append(i)


def bfs(n):
    b = buka[n]
    if len(b) == 0:
        return 1

    salary = [bfs(i) for i in b]
    return max(salary) + min(salary) + 1


ans = bfs(1)
print(ans)
