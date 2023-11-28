times = [tuple(map(int, input().split())) for _ in range(int(input()))]
times.sort(key=lambda x: x[1], reverse=True)
answer = 1000000
for time, end in times:
    answer = min(end, answer) - time
    if answer < 0:
        answer = -1
        break
print(answer)
