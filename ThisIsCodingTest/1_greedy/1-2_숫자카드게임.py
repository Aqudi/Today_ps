N, M = map(int, input().split())
nums = [sorted(list(map(int, input().split()))) for _ in range(N)]
nums = sorted(nums, key=lambda x: x[0], reverse=True)
print(nums[0][0])