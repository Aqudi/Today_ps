def factorial(a, limit):
    result = 1
    for i in range(limit):
        result *= a - i
    return result


N, K = map(int, input().split())
print(factorial(N, K) // factorial(K, K))
