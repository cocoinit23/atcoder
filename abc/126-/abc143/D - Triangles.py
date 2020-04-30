import itertools

n = int(input())
l = map(int, input().split())

comb = list(itertools.combinations(l, 3))

result = 0

for i in range(len(comb)):
    a, b, c = comb[i]
    if a < b + c:
        if b < c + a:
            if c < a + b:
                result += 1

print(result)
