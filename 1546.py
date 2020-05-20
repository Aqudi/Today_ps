N = int(input())
score = list(map(int, input().split()))
M = max(score)
tScore = sum(map(lambda x: x / M * 100, score)) /N
print(tScore)