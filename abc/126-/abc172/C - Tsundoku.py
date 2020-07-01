import bisect

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cum_a = [0]
for i in range(n):
    cum_a.append(cum_a[i] + a[i])

cum_b = [0]
for i in range(m):
    cum_b.append(cum_b[i] + b[i])

ans = 0
val = m
for i in range(n + 1):
    if cum_a[i] > k:
        break

    val = bisect.bisect_right(cum_b, k - cum_a[i]) - 1

    # while cum_b[val] > k - cum_a[i]:
    #    val -= 1

    ans = max(ans, i + val)

print(ans)
