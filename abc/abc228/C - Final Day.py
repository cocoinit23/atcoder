n, k = map(int, input().split())
p = [sum(map(int, input().split())) for _ in range(n)]
border = sorted(p, reverse=True)[k - 1]

for i in p:
    print('Yes' if i + 300 >= border else 'No')
