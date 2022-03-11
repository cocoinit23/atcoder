n = int(input())
a = list(map(int, input().split()))

degree = [0] * 360
degree[0] = 1
for i in a:
    degree = degree[-i:] + degree[:-i]
    degree[0] = 1

angle = []
for i in range(360):
    if degree[i] == 1:
        angle.append(i)
angle.append(360)

ans = 0
for i in range(1, len(angle)):
    ans = max(ans, angle[i] - angle[i - 1])

print(ans)
