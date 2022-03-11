a, b = input().split()

a = sum(map(int, list(a)))
b = sum(map(int, list(b)))

ans = max(a, b)
print(ans)
