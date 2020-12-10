import bisect

n = int(input())
a = sorted(list(map(int, input().split())))
b = list(map(int, input().split()))
c = sorted(list(map(int, input().split())))

ans = 0
for i in b:
    a_pos = bisect.bisect_left(a, i)
    c_pos = n - bisect.bisect_right(c, i)
    ans += a_pos * c_pos

print(ans)
