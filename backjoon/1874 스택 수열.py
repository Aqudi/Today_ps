import sys
N = int(sys.stdin.readline().rstrip())
se = []
for i in range(N):
    se.append(int(sys.stdin.readline().rstrip()))

index, next, last = 0, 1, 0
sem = []
answer = ""
while index < N:
    if next <= se[index]:
        answer += "+\n"
        sem.append(next)
        next += 1
    else:
        answer += "-\n"
        last = sem.pop()
        if se[index] != last:
            sys.stdout.write("NO")
            exit()
        index += 1

if last == se[-1]:
    sys.stdout.write(answer)
