n, q = map(int, input().split())
s = input()
lr = []
for i in range(q):
    lr.append(list(map(int, input().split())))

ac = [0] * n
for i in range(n - 1):
    ac[i + 1] = ac[i] + (1 if s[i:i + 2] == 'AC' else 0)

for i in range(q):
    left = lr[i][0] - 1
    right = lr[i][1] - 1
    ans = ac[right] - ac[left]
    print(ans)
