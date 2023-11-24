# 총 대기 시간을 줄여야하므로 짧은 순으로 먼저 끝내야 함
N = int(input())
ppl = sorted(map(int, input().split()))
for i in range(1, N):
    ppl[i] += ppl[i-1]
print(sum(ppl))