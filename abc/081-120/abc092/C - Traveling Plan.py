n = int(input())
a = [0] + list(map(int, input().split())) + [0]

dist = [abs(a[i + 1] - a[i]) for i in range(len(a) - 1)]
total = sum(dist)

for i in range(1, n + 1):
    ans = total - abs(a[i] - a[i - 1]) - abs(a[i + 1] - a[i]) + abs(a[i - 1] - a[i + 1])
    print(ans)
