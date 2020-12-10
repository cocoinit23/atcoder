n = int(input())
x = 1

takahashi_turn = True

while True:
    if takahashi_turn:
        x *= 2
    else:
        x = 2 * x + 1

    takahashi_turn = not takahashi_turn
    if x > n:
        print('Takahashi') if takahashi_turn else print('Aoki')
        break

