n, m = map(int, input().split())

ans = [-1] * n
flag = True

for i in range(m):
    s, c = map(int, input().split())
    if ans[s - 1] == -1:
        ans[s - 1] = c
    elif ans[s - 1] != c:
        flag = False
        break

if n > 1 and ans[0] == 0:
    flag = False

if not flag:
    print(-1)
    exit()

ans = [0 if i == -1 else i for i in ans]
if n > 1 and ans[0] == 0:
    ans[0] = 1
ans = ''.join(map(str, ans))
print(ans)
