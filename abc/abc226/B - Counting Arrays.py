n = int(input())
la = [list(map(int, input().split())) for _ in range(n)]
a = [tuple(i[1:]) for i in la]

a = set(a)
ans = len(a)

print(ans)
