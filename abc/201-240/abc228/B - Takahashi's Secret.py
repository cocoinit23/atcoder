n, x = map(int, input().split())
a = list(map(int, input().split()))

know = [False] * n

cur = x
while True:
    know[cur - 1] = True
    cur = a[cur - 1]
    if know[cur - 1]:
        break

ans = sum(know)
print(ans)
