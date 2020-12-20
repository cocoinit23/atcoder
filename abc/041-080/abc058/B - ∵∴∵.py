o = input()
e = input()

ans = ''
if len(o) == len(e):
    for i in range(len(o)):
        ans += o[i] + e[i]
elif len(o) > len(e):
    for i in range(len(e)):
        ans += o[i] + e[i]
    ans += o[-1]
else:
    for i in range(len(o)):
        ans += o[i] + e[i]
    ans += e[-1]

print(ans)
