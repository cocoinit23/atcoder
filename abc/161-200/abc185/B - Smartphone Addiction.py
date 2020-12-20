n, m, t = map(int, input().split())

now = 0
battery = n
ans = True
for _ in range(m):
    a, b = map(int, input().split())
    use = a - now
    battery -= use

    if battery <= 0:
        ans = False
        break

    charge = b - a
    battery = min(n, battery + charge)
    now = b

use = t - now
battery -= use
if battery <= 0:
    ans = False

print('Yes') if ans else print('No')
