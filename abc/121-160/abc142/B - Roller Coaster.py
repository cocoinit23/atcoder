n, k = map(int, input().split())
h = input().split()

cnt = 0

for i in range(len(h)):
    if int(h[i]) >= k:
        cnt += 1

print(cnt)
