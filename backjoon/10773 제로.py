K = int(input())
nums = []
for i in range(K):
    n = int(input())
    if n == 0:
        nums.pop()
    else:
        nums.append(n)
print(sum(nums))
