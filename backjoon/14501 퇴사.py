import sys

input = sys.stdin.readline
N = int(input())
TP= []
for _ in range(N):
    tp = tuple(map(int, input().split()))
    TP.append(tp)

dp = [0 for i in range(N+1)]
for i, (t,p) in enumerate(TP):
    for j in range(i + t, N+1):
        dp[j] = max(dp[j], dp[i] + p)
print(dp[-1])