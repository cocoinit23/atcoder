n = int(input())
l = sorted(list(map(int, input().split())))

if l[-1] < sum(l[:-1]):
    print('Yes')
else:
    print('No')
