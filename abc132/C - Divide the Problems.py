n = int(input())
d = list(map(int, input().split()))

d = sorted(d)

x = n // 2

print(d[x] - d[x - 1])
