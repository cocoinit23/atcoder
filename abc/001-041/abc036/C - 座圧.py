n = int(input())
a = [int(input()) for _ in range(n)]

hash = {}
for i, l in enumerate(sorted(set(a))):
    hash[l] = i

for i in a:
    print(hash[i])
