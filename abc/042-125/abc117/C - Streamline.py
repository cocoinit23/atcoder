n, m = map(int, input().split())
x = sorted(list(map(int, input().split())))

if n >= m or m == 1:
    print(0)
else:
    move = sorted([x[i] - x[i - 1] for i in range(1, m)])

    ans = sum(move[:-n + 1]) if n > 1 else sum(move)
    print(ans)
