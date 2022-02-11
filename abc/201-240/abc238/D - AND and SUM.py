t = int(input())

for _ in range(t):
    a, s = map(int, input().split())
    xor = s - 2 * a
    if xor >= 0 and xor & a == 0:
        print('Yes')
    else:
        print('No')
