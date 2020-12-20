n, k = map(int, input().split())
p = sorted(list(map(int, input().split())))

ans = sum(p[:k])
print(ans)
