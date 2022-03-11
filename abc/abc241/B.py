n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in b:
    if i in a:
        a.remove(i)
    else:
        print('No')
        exit()

print('Yes')
