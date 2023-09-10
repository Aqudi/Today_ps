import sys

nums = [int(sys.stdin.readline()) for _ in range(int(input()))]
for i in sorted(nums):
    print(i)
