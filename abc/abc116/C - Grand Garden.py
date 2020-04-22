n = int(input())
h = [int(x) for x in input().split()]

cost = h[0]

for i in range(1, n):
    if h[i - 1] < h[i]:
        cost += h[i] - h[i - 1]

print(cost)
