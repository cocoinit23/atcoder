s1 = list(input())
s2 = list(input())

black = s1.count('#') + s2.count('#')

ans = True
if black == 2:
    if s1 == s2[::-1]:
        ans = False

print('Yes' if ans else 'No')
