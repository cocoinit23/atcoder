val = list(map(int, input().split()))

ans = False
for i in range(2 ** 4):
    pattern = [0] * 4
    for j in range(4):
        if i >> j & 1:
            pattern[j] = 1

    eat = 0
    rest = 0
    for k in range(4):
        if pattern[k] == 0:
            rest += val[k]
        else:
            eat += val[k]
    if eat == rest:
        ans = True
        break

print('Yes') if ans else print('No')
