a, b, c = map(int, input().split())
k = int(input())

ans = False
for x in range(k + 1):
    for y in range(k - x + 1):
        for z in range(k - x - y + 1):
            if a * (2 ** x) < b * (2 ** y) < c * (2 ** z):
                ans = True
                break

print('Yes') if ans else print('No')
