c = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(str(alphabet))):
    if alphabet[i] == c:
        print(alphabet[i + 1])
