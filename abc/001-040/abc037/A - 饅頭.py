a, b, c = map(int, input().split())

ans = 0
ans += c // min(a, b)
c %= min(a, b)
ans += c // max(a, b)
print(ans)
