# DP 문제
# 1x2 추가, 2x1 2개 추가, 2x2 1개 추가

num = int(input())
memo = [0 for i in range(num+1)]
for i in range(1, num+1):
    if i == 1:
        memo[i] = 1
    elif i == 2:
        memo[i] = 3
    elif memo[i] != 0:
        continue
    else:
        memo[i] = memo[i-1] + memo[i-2]*2
print(memo[num] % 10007)
