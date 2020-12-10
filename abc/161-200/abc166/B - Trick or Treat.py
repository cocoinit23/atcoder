n, k = map(int, input().split())
d = []
a = []
for i in range(k):
    d.append(int(input()))
    a.append(list(map(int, input().split())))

ans = [1] * n
for x in a:
    for i in x:
        ans[i - 1] = 0

print(sum(ans))
