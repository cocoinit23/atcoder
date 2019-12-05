import itertools

n = input()
d = map(int, input().split())

c = list(itertools.combinations(d, 2))

result = 0
for i in range(len(c)):
    result += c[i][0] * c[i][1]

print(result)

