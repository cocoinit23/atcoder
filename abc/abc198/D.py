import itertools

s = [input() for _ in range(3)]
letter = sorted(set("".join(s)))

if len(letter) > 10:
    print("UNSOLVABLE")
    exit()

letter = list(letter)
idx = {k: v for v, k in enumerate(letter)}

for perm in itertools.permutations(range(10)):
    num = []
    for x in s:
        initial_letter = x[0]
        if perm[idx[initial_letter]] == 0:
            break
        n = 0
        for i in x:
            n = 10 * n + perm[idx[i]]
        num.append(n)
    if len(num) == 3 and num[0] + num[1] == num[2]:
        for i in num:
            print(i)
        exit()
print("UNSOLVABLE")
