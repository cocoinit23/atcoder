from functools import reduce

n = int(input())
a = list(map(int, input().split()))

all = reduce(lambda x, y: x ^ y, a)
ans = [all ^ i for i in a]
print(*ans)
