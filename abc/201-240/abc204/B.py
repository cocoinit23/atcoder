n = int(input())
a = map(int, input().split())
a = map(lambda x: max(x - 10, 0), a)

ans = sum(a)
print(ans)
