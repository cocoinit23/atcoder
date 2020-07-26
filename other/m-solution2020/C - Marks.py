n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(k, n):
    if a[i - k] / a[i] < 1:
        print('Yes')
    else:
        print('No')
