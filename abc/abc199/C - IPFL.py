n = int(input())
s = input()
q = int(input())

s = list(s)
flip = False
for i in range(q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if t == 2:
        flip = not flip

    if flip:
        if a >= n:
            a -= n
        else:
            a += n

        if b >= n:
            b -= n
        else:
            b += n

    s[a], s[b] = s[b], s[a]

if flip:
    s = s[n:] + s[:n]

ans = ''.join(s)
print(ans)
