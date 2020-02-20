n = int(input())
v = [int(x) for x in input().split()]

v.sort()

while len(v) > 1:
    v[1] = (v[0] + v[1]) / 2
    v = v[1:]

print((v[0]))
