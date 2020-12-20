n = input()

sn = sum(map(int, list(n)))

if int(n) % sn == 0:
    print('Yes')
else:
    print('No')
