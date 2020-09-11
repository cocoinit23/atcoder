sx, sy, tx, ty = map(int, input().split())
dx, dy = tx - sx, ty - sy

print('R' * dx + 'U' * dy + 'L' * dx + 'D' * dy, end='')
print('D' + 'R' * (dx + 1) + 'U' * (dy + 1) + 'L', end='')
print('U' + 'L' * (dx + 1) + 'D' * (dy + 1) + 'R')
