from collections import Counter

n = int(input())
v = list(map(int, input().split()))

if len(set(v)) == 1:
    print(n // 2)
else:
    v1 = [v[i] for i in range(0, n, 2)]
    v2 = [v[i + 1] for i in range(0, n, 2)]

    kw1 = Counter(v1)
    kw2 = Counter(v2)

    x1 = kw1.most_common()[0][0]
    x2 = kw2.most_common()[0][0]

    if x1 != x2:
        ans = 0
        for i in v1:
            if i != x1:
                ans += 1
        for i in v2:
            if i != x2:
                ans += 1
    else:
        y1 = kw1.most_common()[1][0]
        y2 = kw2.most_common()[1][0]

        ans1 = 0
        ans2 = 0

        for i in v1:
            if i != y1:
                ans1 += 1
        for i in v2:
            if i != x2:
                ans1 += 1

        for i in v1:
            if i != x1:
                ans2 += 1
        for i in v2:
            if i != y2:
                ans2 += 1

        ans = min(ans1, ans2)

    print(ans)
