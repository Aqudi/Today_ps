N = int(input())
answer = ""
timers = [300, 60, 10]
for t in timers:
    count = N // t
    N -= count * t
    answer += f"{count} "
if N != 0:
    print(-1)
else:
    print(answer)