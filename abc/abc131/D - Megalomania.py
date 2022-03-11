n = int(input())
job = [list(map(int, input().split())) for _ in range(n)]
job.sort(key=lambda x: x[1])

ans = True
time = 0
for i, j in job:
    time += i
    if time > j:
        ans = False
        break

print("Yes") if ans else print("No")
