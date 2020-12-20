n = int(input())
red = [list(map(int, input().split())) for _ in range(n)]
blue = [list(map(int, input().split())) for _ in range(n)]

red.sort(reverse=True, key=lambda x: x[1])
blue.sort()

ans = 0
for i in range(len(blue)):
    c, d = blue[i]
    for j in range(len(red)):
        a, b = red[j]
        if a < c and b < d:
            del red[j]
            ans += 1
            break
print(ans)
