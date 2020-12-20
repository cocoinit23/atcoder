import copy

h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]

hpattern = []
for i in range(2 ** h):
    temp = [0] * h
    for j in range(h):
        if i >> j & 1:
            temp[j] = 1
    hpattern.append(temp)

wpattern = []
for i in range(2 ** w):
    temp = [0] * w
    for j in range(w):
        if i >> j & 1:
            temp[j] = 1
    wpattern.append(temp)

ans = 0
for hp in hpattern:
    for wp in wpattern:
        cc = copy.deepcopy(c)
        for i in range(h):
            for j in range(w):
                if hp[i] == 1:
                    cc[i][j] = -1
                if wp[j] == 1:
                    cc[i][j] = -1

        black = sum([l.count('#') for l in cc])
        if black == k:
            ans += 1

print(ans)
