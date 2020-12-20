n = int(input())
a = [int(input()) for _ in range(n)]
ans = sorted(set(a))[-2]
print(ans)
