s = input()
ans = True
even = False
for i in s:
    if even and i.isupper():
        even = not even
    elif not even and i.islower():
        even = not even
    else:
        ans = False
        break

print("Yes") if ans else print("No")
