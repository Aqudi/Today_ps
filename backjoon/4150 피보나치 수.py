N = int(input())
memo = [1, 1, 1, *[0 for i in range(N)]]
for i in range(N+1):
    if not memo[i]:
        memo[i] = memo[i-1]+memo[i-2]
print(memo[N])
