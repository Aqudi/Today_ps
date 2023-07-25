N = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
answer = 0
for coin in coins:
    count = N // coin
    N -= coin * count
    answer += count
    if N == 0:
        break
print(answer)
