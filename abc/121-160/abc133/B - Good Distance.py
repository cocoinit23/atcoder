from scipy.spatial import distance
import itertools

n, d = map(int, input().split())

x = []
for i in range(n):
    x.append(list(map(int, input().split())))

combi = list(itertools.combinations(x, 2))

ans = 0
for i in range(len(combi)):
    dis = distance.euclidean(combi[i][0], combi[i][1])
    if dis.is_integer():
        ans += 1

print(ans)
