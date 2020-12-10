k, x = map(int, input().split())

a = [x for x in range(x - k + 1, x + k)]
print(*a)
