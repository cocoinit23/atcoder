n = int(input())
a, b = map(int, input().split())
k = int(input())
p = list(map(int, input().split()))

visited = [a, b] + p
if len(visited) != len(set(visited)):
    print('NO')
else:
    print('YES')
