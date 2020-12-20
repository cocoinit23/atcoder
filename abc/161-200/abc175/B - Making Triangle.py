from itertools import combinations

n = int(input())
l = list(map(int, input().split()))

combi = combinations(l, 3)

ans = 0
for a, b, c in combi:
    if a != b and b != c and c != a:
        if a + b > c and b + c > a and c + a > b:
            ans += 1

print(ans)
