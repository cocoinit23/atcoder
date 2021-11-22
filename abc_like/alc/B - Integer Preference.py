a, b, c, d = map(int, input().split())
if max(a, c) <= min(b, d):
    print("Yes")
else:
    print("No")
