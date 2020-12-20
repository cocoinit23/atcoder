h, w = map(int, input().split())
grid = []
for i in range(h):
    temp = list(input())
    if set(temp) != {'.'}:
        grid.append(temp)


transpose = [list(x) for x in zip(*grid)]

ans = []
for l in transpose:
    if set(l) != {'.'}:
        ans.append(l)

ans = [list(x) for x in zip(*ans)]
for l in ans:
    print(''.join(l))
