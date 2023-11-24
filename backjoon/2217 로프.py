N = int(input())
nums = sorted([int(input()) for i in range(N)], reverse=True)
maxWeights = [n * (i+1) for i, n in enumerate(nums)]
print(max(maxWeights))