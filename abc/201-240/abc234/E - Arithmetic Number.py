x = int(input())

result = set()

for first in range(1, 10):
    for diff in range(-9, 10):
        val = str(first)
        for _ in range(0, 18):
            result.add(int(val))
            addval = int(val[-1]) + diff
            if 0 <= addval <= 9:
                val += str(int(val[-1]) + diff)
            else:
                break

result = sorted(list(result))

l = -1
r = len(result)
while r - l > 1:
    mid = (l + r) // 2
    if result[mid] < x:
        l = mid
    else:
        r = mid

ans = result[r]
print(ans)
