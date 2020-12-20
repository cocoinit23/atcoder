n = int(input())
w = [int(x) for x in input().split()]

ans = 10000000000

for i in range(n):
    left = w[:i]
    right = w[i:]
    ans = min(ans, abs(sum(left) - sum(right)))

print(ans)
