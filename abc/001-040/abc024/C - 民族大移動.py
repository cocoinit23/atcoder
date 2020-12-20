n, d, k = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(d)]
st = [list(map(int, input().split())) for _ in range(k)]

position = [s for s, _ in st]
goal = [t for _, t in st]
ans = [1e9] * k

count = 1
for l, r in lr:
    for i in range(k):
        if l <= position[i] <= r:
            if l <= goal[i] <= r:
                position[i] = goal[i]
            else:
                if position[i] < goal[i]:
                    position[i] = r
                else:
                    position[i] = l

        if position[i] == goal[i]:
            ans[i] = min(ans[i], count)
    count += 1

for a in ans:
    print(a)
