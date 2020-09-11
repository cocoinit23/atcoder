n = int(input())
c = list(input())

s = sorted(c)

cnt = 0
for i, j in zip(c, s):
    if i != j:
        cnt += 1

print(cnt // 2)
