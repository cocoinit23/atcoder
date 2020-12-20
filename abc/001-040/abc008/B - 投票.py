from collections import Counter

n = int(input())
s = [input() for _ in range(n)]
s = Counter(s)
ans, _ = s.most_common()[0]
print(ans)
