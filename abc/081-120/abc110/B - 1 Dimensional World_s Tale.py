n, m, x, y = map(int, input().split())
xx = [int(i) for i in input().split()]
yy = [int(i) for i in input().split()]

war = False
for z in range(x + 1, y + 1):
    if max(xx) < z <= min(yy):
        war = True

print('No War') if war else print('War')
