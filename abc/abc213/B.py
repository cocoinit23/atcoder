n = int(input())
a = list(map(int, input().split()))

booby = sorted(a)[-2]
print(a.index(booby) + 1)
