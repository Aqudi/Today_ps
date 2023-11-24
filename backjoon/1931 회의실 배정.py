# 최대한 많은 회의를 진행하려면 시작시간보다 끝나는 시간이 빨라야 한다.
# 빠르게 끝나는 회의들을 먼저 진행하면 다음 회의를 빠르게 시작 할 수 있다.
N = int(input())
S = [tuple(map(int, input().split())) for i in range(N)]
S.sort(key=lambda x: x[0])
S.sort(key=lambda x: x[1])

answer = 0
lastEnd = 0
for start, end in S:
    if start >= lastEnd:
        answer += 1
        lastEnd = end
print(answer)