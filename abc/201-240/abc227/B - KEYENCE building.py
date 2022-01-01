n = int(input())
s = list(map(int, input().split()))

pred = set()
for a in range(1, 1000):
    for b in range(1, 1000):
        area = 4 * a * b + 3 * a + 3 * b
        if area <= 1000:
            pred.add(area)

ans = 0
for i in s:
    if i not in pred:
        ans += 1

print(ans)
