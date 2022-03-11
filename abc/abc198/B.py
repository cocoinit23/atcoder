n = input()

x = len(n)

i = 0
ans = False
while i <= x:
    if n == n[::-1]:
        ans = True
        break
    n = "0" + n
    i += 1

print("Yes") if ans else print("No")
