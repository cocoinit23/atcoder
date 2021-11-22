n, p = map(int, input().split())
a = list(map(int, input().split()))

ans = sum([i < p for i in a])
print(ans)
