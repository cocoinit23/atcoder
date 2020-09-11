n = int(input())
b = [int(x) for x in input().split()]

a = [b[0]]

for i in range(1, n - 1):
    a.append(min(b[i - 1], b[i]))

a.append(b[n - 2])

print(sum(a))
