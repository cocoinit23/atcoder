n, a, b = map(int, input().split())

ans = 0
for i in range(1, n + 1):
    ans = sum(list(map(int, list(str(i)))))
    if a <= ans <= b:
        ans += i

print(ans)
