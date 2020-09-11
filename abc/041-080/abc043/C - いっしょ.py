n = int(input())
a = sorted(list(map(int, input().split())))

ans = 10 ** 10
for i in range(min(a), max(a) + 1):
    val = sum([(x - i) ** 2 for x in a])
    ans = min(ans, val)

print(ans)
