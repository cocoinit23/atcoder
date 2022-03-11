a, b, c = map(int, input().split())

if a + b == c and a - b != c:
    print('+')
elif a + b != c and a - b == c:
    print('-')
elif a + b == a - b == c:
    print('?')
else:
    print('!')
