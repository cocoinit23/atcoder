x = list(map(int, input().split()))
y = list(map(int, input().split()))
z = list(map(int, input().split()))

a = (sum(x) + sum(y) + sum(z)) / 3
b = x[0] + y[1] + z[2]
c = x[1] + y[2] + z[0]
d = x[2] + y[0] + z[1]

if a == b == c == d:
    print('Yes')
else:
    print('No')
