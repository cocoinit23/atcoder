def base_n_to_10(x: str, n: int) -> int:
    out = 0
    for i in range(1, len(str(x)) + 1):
        out += int(x[-i]) * (n ** (i - 1))
    return out


x = input()
m = int(input())

base = max(map(int, list(x))) + 1
l = base
r = 10 ** 10

while r - l > 1:
    mid = (l + r) // 2
    val = base_n_to_10(x, mid)
    if val > m:
        r = mid
    else:
        l = mid

ans = set()
for i in range(base, r):
    ans.add(base_n_to_10(x, i))
ans = len(ans)
print(ans)
