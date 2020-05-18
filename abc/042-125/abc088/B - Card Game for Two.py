n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)

alice = 0
bob = 0

for i in range(n):
    if i % 2 == 0:
        alice += a[i]
    else:
        bob += a[i]

ans = alice - bob
print(ans)
