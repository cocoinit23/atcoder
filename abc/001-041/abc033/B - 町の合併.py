n = int(input())
sp = [input().split() for _ in range(n)]

total = sum(map(int, [i for _, i in sp]))
ans = list(filter(lambda x: int(x[1]) > total // 2, sp))
print(ans[0][0] if ans else 'atcoder')
