a, b, x = map(int, input().split())

if a > x:
    print('NO')
elif a == x:
    print('YES')
else:
    print('YES') if x - a <= b else print('NO')
