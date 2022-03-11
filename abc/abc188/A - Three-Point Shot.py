x, y = map(int, input().split())

ans = min(x, y) + 3 > max(x, y)
print('Yes') if ans else print('No')
