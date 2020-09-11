from collections import Counter

n = int(input())
a = list(map(int, input().split()))

ans = 0
for key, ans in Counter(a).most_common():
    if key > ans:
        ans += ans
    elif key < ans:
        ans += ans - key

print(ans)
