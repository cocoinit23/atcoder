n = int(input())
p = list(map(int, input().split()))

ans = 0
val = [False] * 200001

for i in p:
    val[i] = True
    while val[ans]:
        ans += 1
    print(ans)
