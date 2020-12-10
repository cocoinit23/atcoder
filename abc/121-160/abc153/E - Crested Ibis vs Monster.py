h, n = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    ab[i].append(ab[i][0] / ab[i][1])

ab.sort(key=lambda x: x[2])
ab.reverse()
print(ab)

dp=[[0]*]