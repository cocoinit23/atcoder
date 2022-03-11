v, t, s, d = map(int, input().split())

if t <= d / v <= s:
    ans = False
else:
    ans = True

print('Yes') if ans else print('No')
