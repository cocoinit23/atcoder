n = int(input())

visited = set()
ans = 0
for i in range(n):
    a = int(input())
    if a in visited:
        ans += 1
    else:
        visited.add(a)
print(ans)
