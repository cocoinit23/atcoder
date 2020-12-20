from collections import deque

n = int(input())
a = list(map(int, input().split()))

reverse = False

ans = deque()
for i in a:
    if reverse:
        ans.appendleft(i)
    else:
        ans.append(i)
    reverse = not reverse

print(*reversed(ans)) if reverse else print(*ans)
