nums = [0 for i in range(int(input()))]
for i in range(len(nums)):
    nums[i] = int(input())

memo = [1, 1, 2] + [0 for i in range(3, max(nums)+1)]
for i in range(3, len(memo)):
    memo[i] = (memo[i-1] + memo[i-2] + memo[i-3]) % 1000000009

for num in nums:
    print(memo[num] % 1000000009)