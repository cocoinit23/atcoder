n = int(input())
s = input()

ans = s[:2]
for x in s[2:]:
    ans += x
    if ans[-3:] == "fox":
        ans = ans[:-3]

ans = len(ans)
print(ans)
