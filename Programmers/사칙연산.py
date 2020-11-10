from sys import maxsize as inf

def cal(memo, arr, i, j):
    if memo[i][j] != -inf:
        return memo[i][j]
    
    result, fn = None, None
    if i >= 1 and arr[i-1] == "-":
        # - 뒤에는 최소값
        result, fn = inf, min
    else:
        # + 뒤에는 최대값
        result, fn = -inf, max
    
    for k in range(i, j, 2):
        # -, + 연산 수행
        if arr[k+1] == "-":
            result = fn(result, cal(memo, arr, i, k) - cal(memo, arr, k+2, j))
        else:
            result = fn(result, cal(memo, arr, i, k) + cal(memo, arr, k+2, j))
        memo[i][j] = result
        
    return memo[i][j]

def solution(arr):
    n = len(arr)
    
    memo = [[-inf for i in range(n)]for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i % 2 == 0:
                memo[i][i] = int(arr[i])

    
    answer = cal(memo, arr, 0, n-1)
    return answer
