h1, w1 = map(int, input().split())
h2, w2 = map(int, input().split())

if w1 == w2 or h1 == w2 or h2 == w1 or h1 == h2:
    print('YES')
else:
    print('NO')
