s = [int(x) for x in list(map(str, input()))]

x = s.count(0)
y = s.count(1)

print(min(x, y) * 2)
