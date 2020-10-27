# DP문제
# 중요한 포인트 : 규칙 찾기 -> 점화식 만들기
# 타일을 붙이는 방법 : 길이 1(1*2 한 개), 길이 2추가(2*1 두 개)

import sys

sys.setrecursionlimit(10**6)
memo = [0 for i in range(1001)]
def dp(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    if memo[x] != 0:
        return memo[x]
    memo[x] = (dp(x-1) + dp(x-2)) % 10007
    return memo[x]
print(dp(int(input())))