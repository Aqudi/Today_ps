times = [tuple(map(int, input().split())) for _ in range(int(input()))]
times.sort(key=lambda x: x[1])

now = 0
answer = 99999999
for time, end in times:
    now += time
    if now > end:
        answer = -1
        break
    answer = min(answer, end - now)
print(answer)
