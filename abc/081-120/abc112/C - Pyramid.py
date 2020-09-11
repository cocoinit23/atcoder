n = int(input())
xyh = [list(map(int, input().split())) for _ in range(n)]

for cx in range(101):
    for cy in range(101):
        for k in range(n):
            x, y, h = xyh[k]
            if h:
                H = h + abs(x - cx) + abs(y - cy)
                break

        ans = True
        for k in range(n):
            x, y, h = xyh[k]
            if h != max(H - abs(x - cx) - abs(y - cy), 0):
                ans = False
                break
        if ans:
            print(cx, cy, H)
            exit()
