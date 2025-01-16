n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
coins = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            coins.append((j, i))

answer = 0
for i in range(n - 3 + 1):
    p1, p2 = i, i+2,

    count = 0
    for coin in coins:
        if p1 <= coin[0] <= p2 and p1 <= coin[1] <= p2:
            count += 1
    
    answer = max(count, answer)

print(answer)