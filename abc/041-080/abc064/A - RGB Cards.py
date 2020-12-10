r, g, b = input().split()

ans = int(r + g + b)
print('YES') if ans % 4 == 0 else print('NO')
