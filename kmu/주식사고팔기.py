def solution(prices):
    money = 0    
    cost = -1
    for i in range(len(prices)-1):
        if cost == -1:
            if i is not len(prices) - 1 and prices[i] <= prices[i+1]:
                cost = prices[i]
                money -= cost
        else:
            if prices[i] > prices[i+1] or i == len(prices) - 1:
                money += prices[i]
                cost = -1
    if cost != -1:
        money += prices[-1]
    return money
    