n = int(input())
a = list(map(int, input().split()))

color = [0] * 8
free = 0
for i in a:
    if i < 3200:
        c = i // 400
        color[c] = 1
    else:
        free += 1

ans = sum(color)
print(max(1, ans), ans + free)
