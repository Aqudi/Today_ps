memo = [1, 1, 2]
for num in range(3, 11):
    memo.append(memo[num-1] + memo[num-2] + memo[num-3])

for i in range(int(input())):
    print(memo[int(input())])
