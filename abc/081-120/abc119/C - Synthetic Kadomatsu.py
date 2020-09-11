N, A, B, C = map(int, input().split())
l = [int(input()) for i in range(N)]


def dfs(cur, a, b, c):
    if cur == N:
        return abs(A - a) + abs(B - b) + abs(C - c) - 30 if min(a, b, c) > 0 else 10 ** 9
    no_add = dfs(cur + 1, a, b, c)
    add_a = dfs(cur + 1, a + l[cur], b, c) + 10
    add_b = dfs(cur + 1, a, b + l[cur], c) + 10
    add_c = dfs(cur + 1, a, b, c + l[cur]) + 10

    return min(no_add, add_a, add_b, add_c)


print(dfs(0, 0, 0, 0))
