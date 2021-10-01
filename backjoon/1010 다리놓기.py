import sys
input = sys.stdin.readline

N = int(input())
memo = [1]


def factorial(n):
    if len(memo) > n:
        return memo[n]
    append = memo.append
    for i in range(len(memo), n+1):
        append(memo[i-1]*i)
    return memo[n]


for i in range(N):
    L, R = map(int, input().split())
    fr = factorial(R)
    fl, flm = factorial(L), factorial(R-L)
    print(fr // fl // flm)
