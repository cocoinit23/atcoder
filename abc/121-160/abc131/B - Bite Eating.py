n, l = map(int, input().split())

apple = [i + l for i in range(n)]
aji = sum(apple)

if 0 in apple:
    print(aji)
elif apple[0] > 0:
    print(aji - min(apple))
else:
    print(aji - max(apple))
