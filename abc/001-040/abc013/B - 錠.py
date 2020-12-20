a = int(input())
b = int(input())

# ans = min(abs(b - a), abs(10 - max(a, b)) + abs(min(a, b) - 0))
ans = min(abs(b - a), 10 - abs(b - a))
print(ans)
