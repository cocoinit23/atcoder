import sys
sys.setrecursionlimit(10000)

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())


def cheak(x, y):
    if x + y == r2 + c2 or x - y == r2 - c2 or abs(x - r2) + abs(y - c2) <= 3:
        return True
    else:
        return False


def search(x, y, cnt):
    if x == r2 and y == c2:
        return cnt

    cnt += 1
    if cheak(x, y):
        return cnt

    if x == r2 and y > c2:
        return search(x, y - 3, cnt)
    elif x == r2 and y < c2:
        return search(x, y + 3, cnt)
    elif x < r2 and y == c2:
        return search(x + 3, y, cnt)
    elif x > r2 and y == c2:
        return search(x - 3, y, cnt)

    if x > r2 and y > c2:
        return search(r2, y - x + r2, cnt)
    elif x > r2 and y < c2:
        return search(r2, y + x - r2, cnt)
    elif x < r2 and y > c2:
        return search(r2, y + x - r2, cnt)
    elif x < r2 and y < c2:
        return search(r2, y - x + r2, cnt)


ans = search(r1, c1, 0)
print(ans)
