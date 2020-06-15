n = int(input())
a = [int(input()) for _ in range(n)]

limit = len(list(set(a)))

hash = {}
for i, l in enumerate(a):
    hash[l] = i

print(hash)
