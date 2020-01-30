n, x = map(int, input().split())
l = [int(x) for x in input().split()]

d = [0] * (n + 1)

for i in range(1, n + 1):
    d[i] = d[i - 1] + l[i - 1]

print(sum(1 for i in d if i <= x))
