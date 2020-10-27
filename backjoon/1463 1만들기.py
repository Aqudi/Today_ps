ni = int(input())
memo = [0 for i in range(ni+1)]
for i in range(2, ni+1):
    memo[i] = 999999999
    if i % 3 == 0:
        temp = memo[i // 3] + 1
        if memo[i] > temp:
            memo[i] = temp
    if i % 2 == 0:
        temp = memo[i // 2] + 1
        if memo[i] > temp:
            memo[i] = temp
    if True:
        temp = memo[i - 1] + 1
        if memo[i] > temp:
            memo[i] = temp
print(memo[ni])

