n = int(input())
a = list(map(int, input().split()))

a = [i for i in a if i != 0]
ans = sum(a) / len(a)
ans = -(-ans // 1)
print(int(ans))
