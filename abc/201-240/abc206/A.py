n = int(input())

n = int(str(n * 1.08).split(".")[0])

if n < 206:
    print("Yay!")
elif n == 206:
    print("so-so")
else:
    print(":(")
