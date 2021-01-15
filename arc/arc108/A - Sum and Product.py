s, p = map(int, input().split())

ans = False
for n in range(int(p ** 0.5) + 1):
    if s - n > 0 and n * (s - n) == p:
        ans = True
        break

print('Yes') if ans else print('No')
