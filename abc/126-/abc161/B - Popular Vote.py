n, m = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)

flag = True
total = sum(a)

for i in range(m):
    if a[i] < total / (4 * m):
        flag = False
        break

print('Yes') if flag else print('No')
