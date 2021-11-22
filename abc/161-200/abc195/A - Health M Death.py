m, h = map(int, input().split())

ans = h % m == 0
print('Yes') if ans else print('No')
