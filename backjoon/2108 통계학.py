import sys

input = sys.stdin.readline
N = int(input())
nums = sorted([int(input()) for _ in range(N)])
total = sum(nums)
length = len(nums)
frequency = {}
for n in nums:
    n = str(n)
    if n not in frequency:
        frequency[n] = 0
    frequency[n] += 1

maxFrequency = 0
frequencyMap = {}
for key, value in frequency.items():
    maxFrequency = max(value, maxFrequency)
    if value not in frequencyMap:
        frequencyMap[value] = []
    frequencyMap[value].append(int(key))


print(int(round(total / length, 0)))
print(nums[length // 2])
mostFrequentNums = frequencyMap[maxFrequency]
if len(mostFrequentNums) != 1:
    mostFrequentNums.sort()
    print(mostFrequentNums[1])
else:
    print(mostFrequentNums[0])
print(nums[-1] - nums[0])
