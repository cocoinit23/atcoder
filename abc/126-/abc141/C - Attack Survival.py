n, k, q = map(int, input().split())

a = []
for i in range(q):
    a.append(int(input()))

point = [k] * n

for i in range(q):
    win = a[i - 1]
    point[win - 1] += 1

point = list(map(lambda x: x - q, point))

for i in range(n):
    if point[i] <= 0:
        print('No')
    else:
        print('Yes')
