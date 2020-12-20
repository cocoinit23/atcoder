n = int(input())
s = list(input().split())

ans = len(set(s))
print('Three') if ans == 3 else print('Four')
