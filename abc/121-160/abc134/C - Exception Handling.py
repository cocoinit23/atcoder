n = int(input())
a = [int(input()) for i in range(n)]

aa = sorted(a)
first = aa[-1]
second = aa[-2]

for i in range(n):
    if a[i] != first:
        print(first)
    else:
        print(second)
