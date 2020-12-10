n, k = map(int, input().split())

cnt = 0

while n // k != 0:
    cnt += 1
    n /= k

print(cnt + 1)
