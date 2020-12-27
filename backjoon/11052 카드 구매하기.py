import math

N = int(input())
P = [0, *map(int, input().split())]
dp = [0, *(P[i] for i in range(N))]
for i in range(1, N+1):
    cost = -math.inf
    for j in range(1, i+1):
        cost = max(cost, P[j] + dp[i -j])
    dp[i] = cost
print(dp[-1])