n = int(input())
a = list(map(int, input().split()))

ans = sorted([[x, i + 1] for i, x in enumerate(a)], reverse=True)
for i in range(n):
    print(ans[i][1])
