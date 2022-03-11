s = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

ans = set(s) ^ set(alphabet)
print(sorted(list(ans))[0]) if len(ans) != 0 else print('None')
