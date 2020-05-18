n = input()

print('Yes') if int(n) % sum(list(map(int, list(n)))) == 0 else print('No')
