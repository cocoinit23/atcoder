b = [list(map(int, input().split())) for _ in range(2)]
c = [list(map(int, input().split())) for _ in range(3)]

board = [[9] * 3 for _ in range(3)]


def calc():
    score = 0
    for i in range(2):
        for j in range(3):
            if board[i][j] == board[i + 1][j]:
                score += b[i][j]

    for i in range(3):
        for j in range(2):
            if board[i][j] == board[i][j + 1]:
                score += c[i][j]

    return score


def dfs(turn):
    if turn == 9:
        return calc()

    if turn % 2 == 0:
        point = -1
        for i in range(3):
            for j in range(3):
                if board[i][j] != 9:
                    continue
                board[i][j] = 0
                point = max(point, dfs(turn + 1))
                board[i][j] = 9

        return point

    else:
        point = 1e10
        for i in range(3):
            for j in range(3):
                if board[i][j] != 9:
                    continue
                board[i][j] = 1
                point = min(point, dfs(turn + 1))
                board[i][j] = 9

        return point


chokudai = dfs(0)
chokuko = sum(map(sum, b)) + sum(map(sum, c)) - chokudai
print(chokudai)
print(chokuko)
