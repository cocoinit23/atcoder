n = int(input())
a = list(map(int, input().split()))

while len(set(a)) != 1:
    a.sort()
    m = a[0]
    a = [i % m if i % m != 0 else i % m + m for i in a]

print(a[0])
