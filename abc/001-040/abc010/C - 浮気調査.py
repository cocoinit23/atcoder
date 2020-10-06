from scipy.spatial.distance import euclidean

txa, tya, txb, tyb, t, v = map(int, input().split())
n = int(input())
flag = False
for _ in range(n):
    x, y = map(int, input().split())
    dist = euclidean((txa, tya), (x, y)) + euclidean((x, y), (txb, tyb))
    if dist <= t * v:
        flag = True
        break

print('YES') if flag else print('NO')
