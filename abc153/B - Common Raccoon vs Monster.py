h, n = map(int, input().split())
a = [int(x) for x in input().split()]

if h <= sum(a):
    print('Yes')
else:
    print('No')
