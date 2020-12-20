c1 = list(input())
c2 = list(input())

print('YES') if (list(reversed(c1)) == c2 and list(reversed(c2)) == c1) else print('NO')
